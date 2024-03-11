from shiny import App

from pyshiny_template.shiny_modules.root import get_ui, server

app_ui = get_ui()

app = App(app_ui, server)
