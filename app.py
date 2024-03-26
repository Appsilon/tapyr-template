import sys
from pathlib import Path

from loguru import logger
from shiny import App, ui

from pyshiny_template.settings import AppSettings
from pyshiny_template.view.root import get_dashboard_ui, server

# Setup settings and logger
app_settings = AppSettings()
logger.remove()
logger.add(sys.stderr, level=app_settings.log_level)

# External resources, like CSS and JS files
# Can be moved to a separate file
google_fonts_tag = ui.TagList(
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Roboto"),
    ui.tags.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Maven+Pro"),
)

# Combine clean shiny UI with CSS and external resources
ui_with_css = ui.TagList(ui.tags.link(href="style.css", rel="stylesheet"), google_fonts_tag, get_dashboard_ui())

app_dir = Path(__file__).parent
app = App(ui_with_css, server, static_assets=app_dir / "www")
