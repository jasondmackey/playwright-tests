"""Verify Playwright setup: browser launches, navigates, and interacts."""
from playwright.sync_api import Page, expect


def test_browser_navigates(page: Page):
    """Browser can load a page and read its title."""
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")


def test_page_content(page: Page):
    """Browser can query DOM content."""
    page.goto("https://example.com")
    heading = page.locator("h1")
    expect(heading).to_have_text("Example Domain")


def test_link_click(page: Page):
    """Browser can click a link and navigate."""
    page.goto("https://example.com")
    page.get_by_role("link", name="Learn more").click()
    expect(page).not_to_have_url("https://example.com")
