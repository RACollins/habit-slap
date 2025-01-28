from fasthtml.common import *
from components import TestimonialCard, PricingCard


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
            "text": "I used to smoke like a chimney before I signed up to Habit Slap. "
            "You couldn't stop me! One after the other, puff, puff, puffing away. "
            "Tommy Tank they used to call me, which I didn't like because that's not my name. "
            "But getting those emails every morning, it's like the cigarette was being slapped right out of my mouth! ",
            "author": "Thomas Walker",
            "username": "tommychoochoowalker",
        },
        {
            "text": "New morning routine: wake up, read email, lock the f*ck in!",
            "author": "Xavier Wickman",
            "username": "saltybread",
        },
        {
            "text": "I look forward to the emails every day. "
            "It's exciting! "
            "Not like that drop-of-the-stomach kind of feeling you get from not realising there's another step before the end of the stair case. "
            "More like that slow burn excitement, "
            "like waiting for your meal kit delivery.",
            "author": "Hannah Rowley",
            "username": "theforestgirl",
        },
        {
            "text": "I'd been meaning to read 12 books a day ever since I was a kid. "
            "But I never could get myself to do it. "
            "Until I started getting these emails every day. "
            "Now I'm reading 12 books a day, and I'm not even trying! "
            "It's like the books are just flying into my brain! ",
            "author": "Mike Rodriguez",
            "username": "mikedev",
        },
        {
            "text": "Wow... I never knew I needed this in my life, "
            "but I'm absolutely addicted. "
            "Motivation up the wazoo!",
            "author": "Sarah Chen",
            "username": "sarahcodes",
        },
        {
            "text": "I've tried many habit tracking apps, "
            "but the email slaps really make a difference. "
            "They're like having a friend who won't let you slack off.",
            "author": "Peter Pickering",
            "username": "peterpickedapieceofpickledpepper",
        },
    ]

    return Container(
        Div(
            H2("Testimonials"),
            P(
                "What our users are saying about us (may be fake)",
                cls="text-center subtitle",
            ),
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
        "Who is this for?": "For those who know what to do to improve, "
        "but lack the motivation to do it.\n"
        "Look, if you're overweight, you know how to lose weight, it's not complicated. "
        "But there are so many hucksters out there trying to sell you their magic pills. "
        "How many times have you seen this?\n"
        "--- 'Take my course on how to make $5k/month in passive income.'\n"
        "--- '7 Secrets of Seduction, hard copy, only $69.69 plus full access to the exclusive community!'\n"
        "--- 'Optimise your water intake with this over engineered water bottle and my water tracking app!'\n"
        "You don't need a course, you don't need an app, you need a slap in the face!\n"
        "Enter Habit Slap ✋💥\n"
        "Simple, no-nonsense, get-out-of-bed-and-make-some-action emails, "
        "sent weekly or daily straight to your inbox.\n"
        "No more excuses, no more procrastination, no more distractions. "
        "Just get sh*t done!",
        "How much does it cost?": "It's free! (paid pro plan coming soon!)\n"
        "Sign up with your email and set a goal.\n"
        "Cancel anytime.",
        "Who writes the emails?": "gpt-4o-mini, but working on a custom model, "
        "and even human written emails (coming soon!)",
        "How often will I recieve emails?": "--- Free plan: weekly\n"
        "--- Pro plan: daily\n"
        "--- Human plan: daily\n"
        "You can set the time of delivery in your account settings.",
    }
    return Container(
        Div(
            H2("FAQ"),
            *[
                Details(
                    Summary(q, role="button", cls="outline"),
                    *[P(a, raw=True) for a in a.split("\n")],
                )
                for q, a in faq_content.items()
            ],
            id="faq",
        )
    )


def Pricing():
    pricing_tiers = {
        "Free": {
            "price": "0",
            "features": [
                "Weekly emails",
                "Custom delivery time",
                "Change goal anytime",
            ],
        },
        "Pro": {
            "price": "20",
            "features": [
                "Everything in Free",
                "Daily emails",
            ],
        },
        "Human": {
            "price": "60",
            "features": [
                "Everything in Pro",
                "Human written emails",
            ],
        },
    }

    return Container(
        Div(
            H2("Pricing"),
            P("Choose the plan that's right for you", cls="text-center subtitle"),
            Div(
                *[
                    PricingCard(
                        tier=tier, price=details["price"], features=details["features"]
                    )
                    for tier, details in pricing_tiers.items()
                ],
                cls="pricing-grid",
            ),
            id="pricing",
        )
    )


def LandingPage():
    return Div(
        # CustomStyle(),
        MainSignUp(),
        HowItWorks(),
        Testimonials(),
        FAQ(),
        Pricing(),
    )
