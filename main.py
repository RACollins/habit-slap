from fasthtml.common import *
from pages.landing import LandingPage

### Set head elements
css_styles = Link(rel="stylesheet", href="/css/styles.css", type="text/css")

### Set up FastHTML app
app, rt = fast_app(live=True, hdrs=[css_styles])


### Set up routes
@rt("/")
def get():
    return Title("Habit Slap"), Container(LandingPage())


serve()
