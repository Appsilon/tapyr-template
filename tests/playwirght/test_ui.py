from conftest import APP_URL
from playwright.sync_api import Page, expect


def test_footer(page: Page):
    page.goto(APP_URL)
    expect(page.get_by_test_id("footer")).to_contain_text("By Appsilon")
