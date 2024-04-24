from shiny import ui


def get_dashboard_ui() -> ui.Tag:
    return ui.page_fluid(
        # We can't use styles with ui.panel_title hance the use of ui.h1 and ui.tags.title
        ui.head_content(ui.tags.title("Tapyr by Appsilon")),
        ui.h1(
            ui.span("Tapyr", style="color: #0099f9;"),
            " | PyShiny Template by ",
            ui.span("Appsilon", style="color: #0099f9;"),
        ),
        ui.card(
            ui.p("Check out the ", ui.a("documentation", href=""), " for quick start guide."),
        ),
        ui.card_footer("By Appsilon with 💙", data_testid="footer"),
    )
