from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_startup(page: Page, app: ShinyAppProc):
    """
    Tests if shiny apps has successfully started.
    """
    page.goto(app.url)

    # Shiny apps require this wait
    page.wait_for_load_state("networkidle")

    # When shiny fails after startup, it adds the #shiny-disconnected-overlay div
    # We check if it's not present in the page
    assert not page.query_selector("#shiny-disconnected-overlay"), "The shiny app failed to start"


def test_startup_without_errors(page: Page, app: ShinyAppProc):
    """
    Tests if shiny app started without errors.
    """
    page.goto(app.url)

    page.wait_for_load_state("networkidle")

    assert not page.query_selector("div.shiny-output-error"), "The shiny app started with errors"


def test_link_button(page: Page, app: ShinyAppProc):
    """
    Test that the link_button contains the link to the docs.
    This is a simple test to show how to use the shiny testing api.
    And probably you want to remove/adjust for your own needs.
    """
    page.goto(app.url)
    # https://shiny.posit.co/py/docs/end-to-end-testing.html
    link_button = controller.OutputUi(page, "link_button")
    link_button.expect.to_contain_text("Start with the docs!")
