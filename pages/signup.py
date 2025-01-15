from fasthtml.common import *


def SignupForm(user):
    return Container(
        Article(
            H1("Welcome to Habit Slap!"),
            P("Let's get you set up with your first goal and email schedule."),
            Form(
                H2("What's your goal?"),
                Textarea(
                    placeholder="I want to...",
                    rows=4,
                    style="margin-bottom: 2rem",
                    name="goal",
                    required=True,
                ),
                H2("When would you like to receive email reminders?"),
                Input(
                    type="datetime-local",
                    name="next_email_date",
                    required=True,
                    style="margin-bottom: 2rem",
                ),
                Button("Complete Setup", cls="primary", type="submit"),
                action="/complete_signup",
                method="post",
            ),
        )
    )
