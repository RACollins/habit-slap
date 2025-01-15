from fasthtml.common import *


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
            H1("Habit Slap", cls="text-center"),
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
            "body": "🏅 Get Shit Done!",
            "bottom": "No more excuses! Build that habit! Attack your week! Also works well for quitting bad habits.",
        },
    }
    return Container(
        Div(
            H2("How it Works", cls="text-center"),
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


def LandingPage():
    return Div(
        # CustomStyle(),
        MainSignUp(),
        HowItWorks(),
    )
