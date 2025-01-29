from fasthtml.common import *
import secrets
from datetime import datetime, timedelta, timezone
import yagmail
import os
from dotenv import load_dotenv
from database.dynamo_handler import DynamoHandler

### Load environment variables
load_dotenv()

from components import TopBar
from pages.landing import LandingPage
from pages.login import MagicLinkForm
from pages.dashboard import Dashboard
from pages.signup import SignupForm


### Initialize database
db = DynamoHandler()


### Set up beforeware
login_redir = RedirectResponse("/login", status_code=303)


def before(req, session):
    auth = req.scope["auth"] = session.get("auth", None)
    # Only redirect to login for protected routes
    if not auth and req.url.path == "/dashboard":
        return login_redir


bware = Beforeware(
    before,
    skip=[
        "/",
        r"/favicon\.ico",
        r"/static/.*",
        r".*\.css",
        "/login",
        "/send_magic_link",
        r"/verify_magic_link/.*",
        "/signup",
        "/complete_signup",
    ],
)

### Set head elements
css_styles = [
    Link(rel="stylesheet", href="/css/styles.css", type="text/css"),
    Script(src="/static/js/modal.js", defer=True),
]


### Set up FastHTML app
app, rt = fast_app(live=True, hdrs=css_styles, before=bware)


### Set up routes
@rt("/")
def get():
    return Title("Habit Slap"), Container(TopBar(), LandingPage())


@rt("/login")
def get():
    return Title("login"), Container(
        TopBar(), MagicLinkForm("Log in", "/send_magic_link")
    )


def send_magic_link_email(email: str, magic_link: str):
    # Get credentials from environment variables
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_PASSWORD")

    email_content = f"""
    Hi there,
  
    Click this link to sign in to The App: {magic_link}
  
    If you didn't request this, just ignore this email.
  
    Cheers,
    The Habit Slap Team
    """

    # Initialize yagmail SMTP client
    yag = yagmail.SMTP(sender_email, sender_password)

    try:
        # Send email
        yag.send(to=email, subject="Sign in to The App", contents=email_content)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
    finally:
        yag.close()


@rt("/send_magic_link")
def post(email: str):
    if not email:
        return "Email is required"

    user = db.get_user(email)
    if not user:
        user = {
            "email": email,
            "is_active": False,
            "magic_link_token": None,
            "magic_link_expiry": None,
            "tier": "free",  # Add default tier when creating user
        }
        db.create_user(user)

    magic_link_token = secrets.token_urlsafe(32)
    magic_link_expiry = datetime.now(timezone.utc) + timedelta(minutes=15)

    db.update_user(
        email,
        {
            "magic_link_token": magic_link_token,
            "magic_link_expiry": magic_link_expiry.isoformat(),
        },
    )

    magic_link = f"https://habit-slap.vercel.app/verify_magic_link/{magic_link_token}"
    send_magic_link_email(email, magic_link)

    return (
        Div(
            P(
                "Check your inbox. Link will expire in 15 minutes.",
                style="text-align: center",
            ),
            style="text-align: center",
        ),
        HttpHeader("HX-Reswap", "outerHTML"),
        Button(
            "Magic link sent",
            type="submit",
            id="submit-btn",
            disabled=True,
            hx_swap_oob="true",
        ),
    )


@rt("/verify_magic_link/{token}")
def get(session, token: str):
    now = datetime.now(timezone.utc)
    user = db.query_by_token(token)

    if user and datetime.fromisoformat(user["magic_link_expiry"]) > now:
        session["auth"] = user["email"]
        db.update_user(
            user["email"],
            {"magic_link_token": None, "magic_link_expiry": None, "is_active": True},
        )
        if not user.get("goal") or not user.get("next_email_date"):
            return RedirectResponse("/signup")
        return RedirectResponse("/dashboard")
    return "Invalid or expired magic link"


@rt("/logout")
def post(session):
    email = session["auth"]  # Get email before deleting from session
    # Update user's active status to False
    db.update_user(email, {"is_active": False})
    del session["auth"]
    return HttpHeader("HX-Redirect", "/login")


@rt("/dashboard")
def get(session):
    user = db.get_user(session["auth"])
    return Title("Dashboard"), Container(TopBar(), Dashboard(user))


@rt("/save_details")
def post(session, next_email_date: str, goal: str):
    email = session["auth"]
    try:
        # Convert local datetime to UTC
        local_dt = datetime.fromisoformat(next_email_date)
        if local_dt.tzinfo is None:
            local_dt = local_dt.astimezone()
        utc_dt = local_dt.astimezone(timezone.utc)

        db.update_user(email, {"next_email_date": utc_dt.isoformat(), "goal": goal})
        return RedirectResponse("/dashboard", status_code=303)
    except Exception as e:
        return f"Error saving details: {str(e)}"


@rt("/signup")
def get(session):
    if not session.get("auth"):
        return RedirectResponse("/login")
    user = db.get_user(session["auth"])
    return Title("Complete Your Setup"), Container(TopBar(), SignupForm(user))


@rt("/complete_signup")
def post(session, next_email_date: str, goal: str):
    if not session.get("auth"):
        return RedirectResponse("/login")

    email = session["auth"]
    try:
        # Convert local datetime to UTC
        local_dt = datetime.fromisoformat(next_email_date)
        if local_dt.tzinfo is None:
            local_dt = local_dt.astimezone()
        utc_dt = local_dt.astimezone(timezone.utc)

        db.update_user(email, {"next_email_date": utc_dt.isoformat(), "goal": goal})
        return RedirectResponse("/dashboard", status_code=303)
    except Exception as e:
        return f"Error saving details: {str(e)}"


@rt("/delete_account")
def post(session):
    if not session.get("auth"):
        return RedirectResponse("/login")

    email = session["auth"]
    try:
        # Delete the user from the database
        db.delete_user(email)
        # Clear the session
        del session["auth"]
        return HttpHeader("HX-Redirect", "/")
    except Exception as e:
        return f"Error deleting account: {str(e)}"


if __name__ == "__main__":
    serve()
