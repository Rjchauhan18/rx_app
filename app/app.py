"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass

# navbar_style = {
#  "background_color": "black",
#  "font_color": "White",
# }


"""Helper functions """

def navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
            rx.image(src="favicon.ico"),
            rx.spacer(),
            rx.spacer(),

            rx.heading("Rahul Chauhan"),
            ),
            rx.spacer(),
            rx.hstack(

            rx.menu(
                rx.link(
                    rx.menu_button("Home"),
                    href="/",

                ),
                rx.spacer(),
                rx.link(
                    rx.menu_button("Pojects"),
                    href="/projects",

                ),
                rx.spacer(),
                rx.link(
                    rx.menu_button("About"),
                    href="/about",

                ),

            ),
            ),
        ),
        # position="fixed",
        width="100%",
        height="5%",
        # style=navbar_style
        # bottom="px",
        # top="0px",
        # z_index="5",
    )

from typing import List

options: List[str] = ["Option 1", "Option 2", "Option 3"]

""" Pages """
def Home() -> rx.Component:
    return rx.vstack(
    navbar(),
    
    rx.spacer(),
    # rx.spacer(),
    # rx.spacer(),


    rx.container(
        rx.vstack(
        rx.heading("Hello,My Name is Rahul Chauhan.  ",size="lg"),
        
        # rx.spacer(),
        rx.spacer(),
        rx.text("I am Pythonist!!!",font_size="2em",),
        

        ),
    ),
    )


def Projects():
    return rx.vstack(
        navbar(),
        rx.text('Projects Page'),
    )
def about():
       
    return  rx.vstack(
        navbar(),
        rx.vstack(
        rx.text('About Page'),
        # mul_sel(),
    ),
    )

# Add state and page to the app.
app = rx.App()
app.add_page(Home,route='/')
app.add_page(about)
app.add_page(Projects,route='/projects')

app.compile()
