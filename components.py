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


def CheckMark():
    return Span("✓", cls="checkmark")


def PricingCard(tier, price, features):
    period = "/email" if tier == "Human" else "/month"
    is_disabled = tier in ["Pro", "Human"]
    
    # Create button element
    button = Button(f"Start {tier}", cls="outline", disabled=is_disabled)
    
    # Wrap in link only if not disabled
    action_element = A(button, href="/login") if not is_disabled else button
    
    return Article(
        H3(tier),
        H2(f"${price}", Span(period, cls="pricing-period")),
        Ul(*[Ul(CheckMark(), feature) for feature in features], cls="pricing-features"),
        action_element,
        cls="pricing-card",
    )
