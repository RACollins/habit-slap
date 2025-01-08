from fasthtml.common import *


def MagicLinkForm(btn_text: str, target: str):
    return Container(
        Article(
            H1("Welcome Back", cls="text-center"),
            Form(
                Group(
                    Input(
                        id="email",
                        type="email",
                        placeholder="Enter your email",
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
