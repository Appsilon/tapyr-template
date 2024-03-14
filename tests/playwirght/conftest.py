import threading

import pytest
import requests
from tenacity import retry, stop_after_delay, wait_fixed
from uvicorn import Config, Server

APP_HOST = "127.0.0.1"
APP_PORT = 8989
APP_URL = f"http://{APP_HOST}:{APP_PORT}"


@retry(wait=wait_fixed(0.5), stop=stop_after_delay(10))
def wait_for_server_to_start(url):
    response = requests.get(url)  # noqa: S113
    response.raise_for_status()  # Will raise an exception if the request is unsuccessful, i.e. server is not ready


def run_server():
    config = Config(app="app:app", host=APP_HOST, port=APP_PORT, log_level="info")
    server = Server(config)
    server.run()


@pytest.fixture(scope="session", autouse=True)
def _shiny_server():
    # Start the server in a background thread
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()

    wait_for_server_to_start(APP_URL)

    return
