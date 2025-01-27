from fasthtml.common import *
from components import TestimonialCard


# Add custom style to override Pico's default theme
def CustomStyle():
    return Style(
        """
    :root {
        --pico-primary: #1565c0;  /* Custom primary color */
        --pico-primary-background: #1976d2;
        --pico-primary-underline: rgba(21, 101, 192, 0.5);
        --pico-primary-hover: #1976d2;
    }
    
    /* Theme toggle switch styling */
    .theme-switch {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .theme-switch span {
        font-size: 1.2rem;
    }
    """
    )


def MainSignUp():
    return Container(
        Article(
            H1("Habit Slap"),
            P(
                "Motivational emails that hit you like a slap in the face ✋💥",
                cls="text-center",
            ),
            A(Button("Get Started", type="button"), href="/login", cls="text-center"),
            P("Scroll down to learn more", cls="text-center small"),
            A("↓", href="#how-it-works", cls="scroll-arrow"),
            cls="main-signup",
        ),
    )


def HIWCard(top, body, bottom):
    return Article(
        Header(top),
        P(body),
        Footer(bottom),
    )


def HowItWorks():
    card_content = {
        "step1": {
            "top": "Step 1",
            "body": "🎯 Set a Goal",
            "bottom": "Sign up with your email and set a goal.",
        },
        "step2": {
            "top": "Step 2",
            "body": "💪 Get Motivated",
            "bottom": "Recieve weekly/daily emails with motivational messages tailored to your goal.",
        },
        "step3": {
            "top": "Step 3",
            "body": "🏅 Get Sh*t Done!",
            "bottom": "No more excuses! Build that habit! Attack your week! Also works well for quitting bad habits.",
        },
    }
    return Container(
        Div(
            H2("How it Works"),
            Div(
                *[
                    HIWCard(
                        top=card_content[f"step{i+1}"]["top"],
                        body=card_content[f"step{i+1}"]["body"],
                        bottom=card_content[f"step{i+1}"]["bottom"],
                    )
                    for i in range(3)
                ],
                cls="grid",
            ),
            id="how-it-works",
        )
    )


def Testimonials():
    testimonials = [
        {
            "text": "The daily motivation keeps me focused on my goals. "
            "Simple but effective!",
            "author": "Sarah Chen",
            "username": "sarahcodes",
        },
        {
            "text": "These are high-quality courses. Trust me. I own around 10 and the price is worth it for the content quality. @EducativeInc came at the right time in my career. I'm understanding topics better than with any book or online video tutorial I've done. Truly made for developers.",
            "author": "Anthony Walker",
            "username": "_webarchitect_",
        },
        {
            "text": "I've tried many habit tracking apps, but the email slaps really make a difference. They're like having a friend who won't let you slack off.",
            "author": "Mike Rodriguez",
            "username": "mikedev",
        },
        {
            "text": "These are high-quality courses. Trust me. I own around 10 and the price is worth it for the content quality. @EducativeInc came at the right time in my career. I'm understanding topics better than with any book or online video tutorial I've done. Truly made for developers.",
            "author": "Anthony Walker",
            "username": "_webarchitect_",
        },
        {
            "text": "The daily motivation keeps me focused on my goals. Simple but effective!",
            "author": "Sarah Chen",
            "username": "sarahcodes",
        },
        {
            "text": "I've tried many habit tracking apps, but the email slaps really make a difference. They're like having a friend who won't let you slack off.",
            "author": "Mike Rodriguez",
            "username": "mikedev",
        },
    ]

    return Container(
        Div(
            H2("Testimonials"),
            P("What our users are saying about us", cls="text-center subtitle"),
            Div(
                *[
                    TestimonialCard(
                        text=t["text"], author=t["author"], username=t["username"]
                    )
                    for t in testimonials
                ],
                cls="grid",
            ),
            id="testimonials",
        )
    )


def FAQ():
    faq_content = {
        "What is this?": "This is a test",
        "How does it work?": "This is a test",
        "What is the catch?": "This is a test",
        "What if I don't want to receive emails?": "This is a test",
    }
    return Container(
        Div(
            H2("FAQ"),
            *[
                Details(
                    Summary(q, role="button", cls="outline"),
                    P(a),
                )
                for q, a in faq_content.items()
            ],
            id="faq",
        )
    )


def LandingPage():
    return Div(
        # CustomStyle(),
        MainSignUp(),
        HowItWorks(),
        Testimonials(),
        FAQ(),
    )
