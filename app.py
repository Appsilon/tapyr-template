import sys

from loguru import logger
from shiny import App

from pyshiny_template.config import AppConfig
from pyshiny_template.shiny_modules.root import get_ui, server

app_config = AppConfig()
logger.remove()
logger.add(sys.stderr, level=app_config.log_level)


app_ui = get_ui()

app = App(app_ui, server)
