from fasthtml.common import *
import random


def MagicLinkForm(btn_text: str, target: str):
    with open("placeholder_emails.txt", "r") as file:
        placeholder_emails = file.readlines()
    placeholder_email = random.choice(placeholder_emails).strip()
    return Container(
        Article(
            H1("No Passwords. No Excuses.", cls="text-center"),
            P("Just enter your @ and click on the link.", cls="text-center"),
            Form(
                Group(
                    Input(
                        id="email",
                        type="email",
                        placeholder=placeholder_email,
                        required=True,
                    ),
                ),
                Button(btn_text, type="submit", id="submit-btn"),
                P(id="error", cls="error-message"),
                hx_post=target,
                hx_target="#error",
                hx_disabled_elt="#submit-btn",
                cls="text-center",
            ),
            cls="main-signup",
        )
    )
