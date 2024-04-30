from conftest import APP_URL
from playwright.sync_api import Page, expect


def test_startup(page: Page):
    page.goto(APP_URL)
    expect(page).not_to_have_title("404")


def test_footer(page: Page):
    """
    Test that the footer contains the link to the docs.
    This is a simple test to show how to use the `get_by_test_id` method.
    And probably you want to remove/adjust for your own needs.
    """
    page.goto(APP_URL)
    expect(page.get_by_test_id("docs-link")).to_contain_text("Start with the docs!")
