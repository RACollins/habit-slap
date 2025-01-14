from fasthtml.common import *


def Dashboard(user):
    return Container(
        Article(
            Grid(
                H1("Dashboard"),
                Div(
                    P(f"Signed in as {user.email}", style="margin: 0"),
                    A("Not you? logout", href="/login", style="font-size: 0.875rem"),
                    style="text-align: right",
                ),
            ),
            Div(
                P(f"Plan: {user.plan or 'free'}", style="margin-top: 1rem; margin-bottom: 0"),
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
                    Span(f"Next email: {user.next_email_date or 'Not scheduled'}"),
                ),
            ),
            Form(
                H2("Adjust your email schedule", style="margin-top: 1rem"),
                Input(
                    type="datetime-local", 
                    value=user.next_email_date or "", 
                    name="next_email_date",
                    style="margin-top: 1rem; margin-bottom: 2rem"
                ),
                H2("Adjust your goal", style="margin-top: 1rem"),
                Textarea(
                    user.goal or "Set your goal...", 
                    rows=4, 
                    style="margin-bottom: 1rem",
                    name="goal"
                ),
                Grid(
                    Button(
                        "Save Details", 
                        cls="primary",
                        type="submit"
                    ),
                    A(
                        "Upgrade to Premium",
                        href="#",
                        role="button",
                        cls="outline secondary",
                    ),
                ),
                action="/save_details",
                method="post"
            ),
        )
    )
