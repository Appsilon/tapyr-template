from collections.abc import Generator

import pytest
from loguru import logger


class LogSink:
    """Custom log sink to capture log messages from loguru."""

    def __init__(self):
        self.messages = []

    def __call__(self, message):
        self.messages.append(message)


@pytest.fixture()
def loguru_sink() -> Generator[LogSink, None, None]:
    """Fixture to capture log messages from loguru."""
    sink = LogSink()
    logger.remove()
    logger.add(sink)
    yield sink
    logger.remove()
