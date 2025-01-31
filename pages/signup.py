from fasthtml.common import *

MAX_GOAL_LENGTH = 1000


def SignupForm(user):
    return Container(
        Article(
            H1("Welcome to Habit Slap!"),
            P("Let's get you set up with your first goal and email schedule."),
            Form(
                H2("What's your goal?"),
                Div(
                    Textarea(
                        user.get("goal") or "Set your goal...",
                        rows=4,
                        style="margin-bottom: 0.5rem",
                        name="goal",
                        maxlength=str(MAX_GOAL_LENGTH),
                        required=True,
                        oninput="this.nextElementSibling.querySelector('span').textContent = this.value.length",
                    ),
                    P(
                        Span(
                            len(user.get("goal", "")),
                            style="font-weight: bold",
                        ),
                        "/",
                        str(MAX_GOAL_LENGTH),
                        style="text-align: right; font-size: 0.875rem; color: var(--muted-color); margin: 0 0 1rem 0",
                    ),
                ),
                H2("When would you like to receive your emails?"),
                Fieldset(
                    Label(
                        Input(
                            "Daily",
                            type="radio",
                            name="email_frequency",
                            value="daily",
                            disabled=True,
                            data_tooltip="Premium tier feature",
                        )
                    ),
                    Label(
                        Input(
                            "Weekly",
                            type="radio",
                            name="email_frequency",
                            value="weekly",
                            checked=True,
                        )
                    ),
                ),
                Select(
                    Option("Monday"),
                    Option("Tuesday"),
                    Option("Wednesday"),
                    Option("Thursday"),
                    Option("Friday"),
                    Option("Saturday"),
                    Option("Sunday"),
                    name="next_email_day",
                    required=True,
                ),
                Input(
                    type="time",
                    name="next_email_time",
                    required=True,
                    style="margin-bottom: 2rem",
                ),
                Button("Complete Setup", cls="primary", type="submit"),
                action="/complete_signup",
                method="post",
            ),
        )
    )
