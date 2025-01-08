from fasthtml.common import *
from components import TopBar
from pages.landing import LandingPage
from pages.login import MagicLinkForm

### Set head elements
css_styles = Link(rel="stylesheet", href="/css/styles.css", type="text/css")

### Set up FastHTML app
app, rt = fast_app(live=True, hdrs=[css_styles])


### Set up routes
@rt("/")
def get():
    return Title("Habit Slap"), Container(TopBar(), LandingPage())


@rt("/login")
def get():
    return Title("login"), Container(
        TopBar(), MagicLinkForm("Sign In with Email", "/send_magic_link")
    )


serve()
