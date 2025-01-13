from fasthtml.common import *


def Dashboard(email):
    return Nav(
        Div(
            Ul(
                Li(A("Dashboard", href="#")),
                Li(
                    A("About", href="#"),
                ),
                Li(A("Contact", href="#")),
            ),
        ),
        Div(
            Div(
                Button("Logout", cls="uk-button uk-button-primary", hx_post="/logout"),
            ),
        ),
        uk_navbar=True,
    ), Div(
        Div(
            H1(
                "Dashboard",
            ),
            P(f"You are logged in as '{email}'"),
        ),
    )
