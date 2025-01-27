from fasthtml.common import *


def ThemeToggle():
    return Div(
        Span("🌙"),  # Moon icon
        Input(
            type="checkbox",
            role="switch",
            onclick="document.documentElement.setAttribute('data-theme', document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light')",
        ),
        Span("☀️"),  # Sun icon
        cls="theme-switch",
    )


def TopBar():
    return Nav(
        Ul(
            Li(Strong(A("Habit Slap", href="/"))),
        ),
        Ul(
            # Li(ThemeToggle()),
            Li(A("Login", href="/login")),
        ),
    )


def TestimonialCard(text, author, username):
    return Article(
        Blockquote(
            P(text),
            Footer(
                P(
                    Strong(author),
                    Br(),
                    Em(f"@{username}"),
                )
            ),
        ),
        cls="testimonial-card",
    )
