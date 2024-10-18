from shiny import Inputs, Outputs, Session, render, ui


def server(input: Inputs, output: Outputs, session: Session):
    @render.ui
    def link_button():
        """
        UI link that looks like a button. This element could be placed directly in the UI definition
        but is here to showcase testing.
        """
        return ui.a(
            "Start with the docs!",
            href="https://appsilon.github.io/tapyr-docs/",
            target="_blank",
            class_="docs-link",
        )
