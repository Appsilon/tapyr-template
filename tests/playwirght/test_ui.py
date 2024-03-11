from conftest import APP_URL
from playwright.sync_api import Page, expect


def test_div_main(page: Page):
    page.goto(APP_URL)
    expect(page.get_by_test_id("main")).to_contain_text("This is a simple Shiny app.")
