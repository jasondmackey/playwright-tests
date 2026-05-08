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
    heading = page.get_by_role("heading", level=1)
    expect(heading).to_be_visible()


def test_form_interaction(page: Page):
    """Fill out and submit a form on httpbin."""
    page.goto("https://httpbin.org/forms/post")

    page.get_by_label("Customer name").fill("Test User")
    page.get_by_label("Telephone").fill("555-1234")
    page.get_by_label("E-mail address").fill("test@example.com")
    page.get_by_role("radio", name="Medium").check()
    page.get_by_role("checkbox", name="Extra Cheese").check()
    page.get_by_label("Delivery instructions").fill("E2E test order")

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
