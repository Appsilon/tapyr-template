from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import ShinyAppProc


def test_startup2(page: Page, app: ShinyAppProc):
    page.goto(app.url)

    # Wait for the page to load fully
    page.wait_for_load_state("networkidle")

    # Check if the `#shiny-disconnected-overlay` element is not present
    assert not page.query_selector("#shiny-disconnected-overlay"), "The shiny app failed to start"


def test_footer(page: Page, app: ShinyAppProc):
    """
    Test that the footer contains the link to the docs.
    This is a simple test to show how to use the shiny testing api.
    And probably you want to remove/adjust for your own needs.
    """
    page.goto(app.url)
    footer = controller.OutputUi(page, "footer")
    footer.expect.to_contain_text("Start with the docs!")
