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
