from shiny import ui


def get_dashboard_ui() -> ui.Tag:
    return ui.page_fluid(
        # This example shows how custom PyShiny apps can be!
        ui.card(
            ui.row(
                ui.column(
                    7,
                    ui.h1(
                        ui.span("Tapyr", style="color: #486590; font-size: 3rem;"),
                        " | PyShiny Template by ",
                        ui.span("Appsilon", style="color: #007bff; font-size: 3rem;"),
                    ),
                    ui.a(
                        "Start with the docs!",
                        href="https://connect.appsilon.com/tapyr-docs/",
                        class_="docs-link",
                        data_testid="docs-link",
                    ),
                    style="padding: 2rem;",
                ),
                ui.column(
                    5,
                    ui.img(src="images/tapyr.png", style="width: 300px; display: block; margin: 0 auto;"),
                ),
            ),
        ),
        style="display: flex; justify-content: center; align-items: center; height: 100vh;",
    )
