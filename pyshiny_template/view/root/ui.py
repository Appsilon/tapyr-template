from shiny import ui


def get_ui():
    return ui.page_fluid(
        ui.panel_title("Hello world!"),
        ui.div(
            ui.p("This is a simple Shiny app."),
            data_testid="main",
        ),
    )
