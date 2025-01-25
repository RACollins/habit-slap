from fasthtml.common import *
from datetime import datetime, timezone, timedelta

def get_next_sunday_midnight():
    today = datetime.now()
    days_until_sunday = (6 - today.weekday()) % 7
    # If it's Sunday, we want next Sunday unless it's exactly midnight
    if days_until_sunday == 0 and today.time() != datetime.min.time():
        days_until_sunday = 7
    
    # Get next Sunday at midnight
    next_sunday = today + timedelta(days=days_until_sunday)
    # Set time to midnight (00:00:00)
    next_sunday = next_sunday.replace(hour=0, minute=0, second=0, microsecond=0)
    return next_sunday

def Dashboard(user):
    # Convert UTC time to local time for display
    next_email = user.get("next_email_date")
    if next_email:
        utc_dt = datetime.fromisoformat(next_email)
        local_dt = utc_dt.astimezone()  # Converts to local timezone
        next_email = local_dt.strftime(
            "%Y-%m-%dT%H:%M"
        )  # Format for datetime-local input

    # Get next Sunday at midnight in local time
    max_date = get_next_sunday_midnight().strftime("%Y-%m-%dT%H:%M")

    return Container(
        Article(
            Grid(
                H1("Dashboard"),
                Div(
                    P(f"Signed in as {user['email']}", style="margin: 0"),
                    A(
                        "Not you? Logout",
                        href="#",
                        hx_post="/logout",
                        style="font-size: 0.875rem",
                    ),
                    style="text-align: right",
                ),
            ),
            Div(
                P(
                    f"Plan: {user.get('plan') or 'free'}",
                    style="margin-top: 1rem; margin-bottom: 0",
                ),
                A(
                    "Upgrade to Premium",
                    href="/#",
                    style="font-size: 0.875rem",
                ),
                style="margin-bottom: 1rem",
            ),
            H2("Email notifications"),
            Details(
                Summary("Show email schedule", role="button", cls="outline"),
                Div(
                    Span(
                        f"Next email: {local_dt.strftime('%Y-%m-%d %H:%M') if next_email else 'Not scheduled'}"
                    ),
                ),
            ),
            Form(
                H2("Adjust your email schedule", style="margin-top: 1rem"),
                Input(
                    type="datetime-local",
                    value=next_email or "",
                    name="next_email_date",
                    style="margin-top: 1rem; margin-bottom: 2rem",
                    # step="300",
                    max=max_date,
                ),
                H2("Adjust your goal", style="margin-top: 1rem"),
                Textarea(
                    user.get("goal") or "Set your goal...",
                    rows=4,
                    style="margin-bottom: 1rem",
                    name="goal",
                ),
                Grid(
                    Button("Save Details", cls="primary", type="submit"),
                    A(
                        "Upgrade to Premium",
                        href="#",
                        role="button",
                        cls="outline secondary",
                    ),
                ),
                action="/save_details",
                method="post",
            ),
            Details(
                Summary(
                    "Delete Account",
                    role="button",
                    cls="outline",
                    style="margin-top: 2rem; color: var(--pico-del-color);",
                ),
                Div(
                    P(
                        "Warning: This action cannot be undone.",
                        style="color: var(--pico-del-color);",
                    ),
                    Button(
                        "Delete My Account",
                        cls="contrast",
                        style="background-color: var(--pico-del-color); border-color: var(--pico-del-color);",
                        data_target="delete-modal",
                        onclick="toggleModal(event)",
                    ),
                ),
            ),
            Dialog(
                Article(
                    H3("Confirm Account Deletion"),
                    P(
                        "Are you sure you want to delete your account? This action cannot be undone."
                    ),
                    Footer(
                        Button(
                            "Cancel",
                            cls="secondary",
                            onclick="closeModal(visibleModal)",
                        ),
                        Button(
                            "Delete Account",
                            cls="contrast",
                            style="background-color: var(--pico-del-color); border-color: var(--pico-del-color);",
                            hx_post="/delete_account",
                            hx_confirm="This will permanently delete your account. Are you absolutely sure?",
                        ),
                    ),
                ),
                id="delete-modal",
            ),
        )
    )
