"""End-to-end tests exercising multi-step browser interactions."""
import re
from playwright.sync_api import Page, expect


def test_search_and_navigate(page: Page):
    """Use Wikipedia: search for a term, click a result, verify content."""
    page.goto("https://en.wikipedia.org")
    search_box = page.get_by_role("searchbox", name="Search Wikipedia")
    search_box.fill("Playwright (software)")
    search_box.press("Enter")

    expect(page).to_have_title(re.compile("Playwright"))
    heading = page.locator("#firstHeading")
    expect(heading).to_be_visible()


def test_form_interaction(page: Page):
    """Fill out and submit a form on httpbin."""
    page.goto("https://httpbin.org/forms/post")

    page.locator("input[name='custname']").fill("Test User")
    page.locator("input[name='custtel']").fill("555-1234")
    page.locator("input[name='custemail']").fill("test@example.com")
    page.locator("input[name='size'][value='medium']").check()
    page.locator("input[name='topping'][value='cheese']").check()
    page.locator("textarea[name='comments']").fill("E2E test order")

    page.get_by_role("button", name="Submit order").click()
    expect(page).to_have_url(re.compile(r"httpbin\.org/post"))


def test_navigation_history(page: Page):
    """Verify forward/back navigation works across pages."""
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")

    page.goto("https://httpbin.org")
    expect(page).to_have_url("https://httpbin.org/")

    page.go_back()
    expect(page).to_have_url("https://example.com/")

    page.go_forward()
    expect(page).to_have_url("https://httpbin.org/")
