from shiny import Inputs, Outputs, Session, render, ui


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    def footer():
        return ui.a(
            "Start with the docs!",
            href="https://connect.appsilon.com/tapyr-docs/",
            class_="docs-link",
        )
