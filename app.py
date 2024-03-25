import sys

from loguru import logger
from shiny import App

from pyshiny_template.settings import AppSettings
from pyshiny_template.view.root import get_ui, server

app_settings = AppSettings()
logger.remove()
logger.add(sys.stderr, level=app_settings.log_level)


app_ui = get_ui()

app = App(app_ui, server)
