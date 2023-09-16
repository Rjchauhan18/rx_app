# """Welcome to Reflex! This file outlines the steps to create a basic app."""
# from rxconfig import config

import reflex as rx

# docs_url = "https://reflex.dev/docs/getting-started/introduction"
# filename = f"{config.app_name}/{config.app_name}.py"


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

"""
Traceback (most recent call last):
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/bin/reflex", line 5, in <module>
Sep 16 10:19:44 PM      from reflex.reflex import cli
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/__init__.py", line 8, in <module>
Sep 16 10:19:44 PM      from . import el as el
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/el/__init__.py", line 3, in <module>
Sep 16 10:19:44 PM      from .elements import *
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/el/elements/__init__.py", line 4, in <module>
Sep 16 10:19:44 PM      from reflex.el.element import Element
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/el/element.py", line 5, in <module>
Sep 16 10:19:44 PM      from reflex.components.component import Component
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/__init__.py", line 7, in <module>
Sep 16 10:19:44 PM      from .datadisplay import *
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/datadisplay/__init__.py", line 4, in <module>
Sep 16 10:19:44 PM      from .code import Code, CodeBlock
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/datadisplay/code.py", line 6, in <module>
Sep 16 10:19:44 PM      from reflex.components.forms import Button
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/forms/__init__.py", line 18, in <module>
Sep 16 10:19:44 PM      from .iconbutton import IconButton
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/forms/iconbutton.py", line 3, in <module>
Sep 16 10:19:44 PM      from reflex.components.typography.text import Text
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/typography/__init__.py", line 7, in <module>
Sep 16 10:19:44 PM      from .markdown import Markdown
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/components/typography/markdown.py", line 6, in <module>
Sep 16 10:19:44 PM      from reflex.compiler import utils
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/compiler/utils.py", line 25, in <module>
Sep 16 10:19:44 PM      from reflex.state import Cookie, LocalStorage, State
Sep 16 10:19:44 PM    File "/opt/render/project/src/.venv/lib/python3.7/site-packages/reflex/state.py", line 1167
Sep 16 10:19:44 PM      /,
Sep 16 10:19:44 PM      ^

"""

# Add state and page to the app.
app = rx.App()
app.add_page(Home,route='/')
app.add_page(about)
app.add_page(Projects,route='/projects')

app.compile()
