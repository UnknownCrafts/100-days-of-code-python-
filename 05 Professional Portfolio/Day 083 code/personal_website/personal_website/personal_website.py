import reflex as rx

from rxconfig import config

@rx.page(route="/", title="Surya's Website")
def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.vstack(
                rx.heading("Hello World,", size="9"),
                rx.text(
                    "this is Surya Vasudev.",
                    size="5",
                    text_shadow="4px 4px 8px rgba(0,0,0,0.8)"
                ),
                rx.text( 
                    "A Student Pursuing Computer Engineering.",
                    size="5",
                    text_shadow="4px 4px 8px rgba(0,0,0,0.8)"
                ),
                rx.text(
                    "Living on the Bleeding Edge of Tech.",
                    size="5",
                    text_shadow="4px 4px 8px rgba(0,0,0,0.8)"
                ),
                spacing= "2",
                justify="center",
                min_height="80vh",
                margin="0px 0px 0px 20px"
            ),
            background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), center/cover url('/cpu.jpeg')",
            box_shadow="inset 0 0 1000px rgba(0,0,0,0.8)",
            border_radius="5%",
            margin= "0px 0px 30px 0px",
        ),
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(src="/folder-open.png"),
                    rx.box(
                        rx.heading("Projects"),
                        rx.text(
                            "Go Check Out My Personal Projects!"
                        ),
                    ),
                    spacing="2",
                ),
                href="/projects",
                underline="none",
            ),
            as_child=True,
        ),
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(src="/github.png"),
                    rx.box(
                        rx.heading("Github"),
                        rx.text(
                            "Look At My Work!"
                        ),
                    ),
                    spacing="2",
                ),
                href="https://github.com/UnknownCrafts",
                underline="none",
            ),
            as_child=True,
        ),
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(src="/linkedin.png"),
                    rx.box(
                        rx.heading("Linkedin"),
                        rx.text(
                            "Connect With Me!"
                        ),
                    ),
                    spacing="2",
                ),
                href="https://www.linkedin.com/in/surya-vasudev-b12547239/",
                underline="none",
            ),
            as_child=True,
        ),
    )
    
@rx.page(route="/projects", title="Projects")
def projects() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("This Page is Still Under Construction!", size="9"),
            rx.text(
                "Please Check Back Later.",
                size="5",
            ),
            spacing= "2",
            justify="center",
            min_height="100vh",
        ),
    )

app = rx.App()
