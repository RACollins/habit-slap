from fasthtml.common import *
import secrets
from datetime import datetime, timedelta
import yagmail
import os
from dotenv import load_dotenv

### Load environment variables
load_dotenv()

from components import TopBar
from pages.landing import LandingPage
from pages.login import MagicLinkForm
from pages.dashboard import Dashboard
from pages.signup import SignupForm


### Initialize database
db = database("data/users_magic_link.db")

SQL_CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
   email TEXT PRIMARY KEY NOT NULL,
   magic_link_token TEXT,
   magic_link_expiry TIMESTAMP,
   is_active BOOLEAN DEFAULT FALSE,
   next_email_date TEXT,
   goal TEXT,
   plan TEXT DEFAULT 'free'
);
"""

db.execute(SQL_CREATE_USERS)
users = db.t.users
User = users.dataclass()


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
css_styles = Link(rel="stylesheet", href="/css/styles.css", type="text/css")


### Set up FastHTML app
app, rt = fast_app(live=True, hdrs=[css_styles], before=bware)


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

    try:
        user = users[email]
    except NotFoundError:
        user = User(
            email=email, is_active=False, magic_link_token=None, magic_link_expiry=None
        )
        users.insert(user)

    magic_link_token = secrets.token_urlsafe(32)
    magic_link_expiry = datetime.now() + timedelta(minutes=15)

    users.update(
        {
            "email": email,
            "magic_link_token": magic_link_token,
            "magic_link_expiry": magic_link_expiry,
        }
    )

    magic_link = f"http://0.0.0.0:5001/verify_magic_link/{magic_link_token}"

    send_magic_link_email(email, magic_link)

    return (
        Div(
            P("Check your inbox. Link will expire in 15 minutes.", style="text-align: center"),
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
    now = datetime.now()
    try:
        user = users(
            where=f"magic_link_token = '{token}' AND magic_link_expiry > '{now}'"
        )[0]
        session["auth"] = user.email
        users.update(
            {
                "email": user.email,
                "magic_link_token": None,
                "magic_link_expiry": None,
                "is_active": True,
            }
        )
        if not user.goal or not user.next_email_date:
            return RedirectResponse("/signup")
        return RedirectResponse("/dashboard")
    except IndexError:
        return "Invalid or expired magic link"


@rt("/logout")
def post(session):
    del session["auth"]
    return HttpHeader("HX-Redirect", "/login")


@rt("/dashboard")
def get(session):
    u = users[session["auth"]]
    return Title("Dashboard"), Container(TopBar(), Dashboard(u))


@rt("/save_details")
def post(session, next_email_date: str, goal: str):
    email = session["auth"]
    try:
        users.update({"email": email, "next_email_date": next_email_date, "goal": goal})
        return RedirectResponse("/dashboard", status_code=303)
    except Exception as e:
        return f"Error saving details: {str(e)}"


@rt("/signup")
def get(session):
    if not session.get("auth"):
        return RedirectResponse("/login")
    u = users[session["auth"]]
    return Title("Complete Your Setup"), Container(TopBar(), SignupForm(u))


@rt("/complete_signup")
def post(session, next_email_date: str, goal: str):
    if not session.get("auth"):
        return RedirectResponse("/login")

    email = session["auth"]
    try:
        users.update({"email": email, "next_email_date": next_email_date, "goal": goal})
        return RedirectResponse("/dashboard", status_code=303)
    except Exception as e:
        return f"Error saving details: {str(e)}"


if __name__ == "__main__":
    serve()
