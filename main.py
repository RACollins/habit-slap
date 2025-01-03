from fasthtml.common import *
from pages.landing import LandingPage

app, rt = fast_app()


### Set up routes
@rt("/")
def get():
    return (Title("Habit Slap"), Container(LandingPage()))


serve()
