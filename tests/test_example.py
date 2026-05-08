"""Example test to verify Playwright setup."""
import re
from playwright.sync_api import Page, expect


def test_homepage_has_title(page: Page):
    """Navigate to Playwright's site and verify the title."""
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


def test_homepage_has_get_started_link(page: Page):
    """Verify the Get Started link is visible."""
    page.goto("https://playwright.dev/")
    get_started = page.get_by_role("link", name="Get started")
    expect(get_started).to_be_visible()
