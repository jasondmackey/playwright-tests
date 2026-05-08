# Playwright Tests

Browser-based automated testing with [Playwright](https://playwright.dev/) and pytest.

## Prerequisites

- Python 3.11+
- pip
- macOS, Linux, or Windows

## Setup

1. Clone the repository:

```sh
git clone https://github.com/jasondmackey/playwright-tests.git
cd playwright-tests
```

2. Install the project and dependencies:

```sh
pip install -e .
```

3. Install browsers for Playwright:

```sh
# Chromium only (default)
playwright install chromium

# All supported browsers
playwright install chromium firefox webkit
```

> **Note (macOS):** If `playwright` is not found, you may need to add the Python user bin directory to your PATH:
>
> ```sh
> export PATH="$HOME/Library/Python/3.13/bin:$PATH"
> ```
>
> Add this to your `~/.zshrc` to make it permanent.

## Running Tests

```sh
# Run all tests (headless, default browser: chromium)
pytest

# Run with a specific browser
pytest --browser firefox
pytest --browser webkit

# Run with all browsers
pytest --browser chromium --browser firefox --browser webkit

# Run with visible browser
pytest --headed

# Run a specific test file
pytest tests/test_e2e.py

# Run a specific test by name
pytest -k "test_form_interaction"

# Verbose output
pytest -v
```

## Test Suites

- **test_example.py** — Basic tests against [playwright.dev](https://playwright.dev/) (title check, link visibility)
- **test_setup_verify.py** — Setup verification against [example.com](https://example.com) (navigation, DOM queries, link clicks)
- **test_e2e.py** — End-to-end tests covering multi-step flows:
  - Wikipedia search and result verification
  - Form fill and submission on httpbin
  - Browser back/forward navigation history

## CI

Tests run automatically via GitHub Actions on every push and pull request to `main` across three browsers (Chromium, Firefox, WebKit) in parallel. You can also trigger a run manually from the [Actions tab](https://github.com/jasondmackey/playwright-tests/actions).

On failure, screenshots and Playwright traces are uploaded as artifacts per browser.

## Writing New Tests

Add test files to the `tests/` directory with a `test_` prefix. Each test function receives a Playwright `page` fixture automatically:

```python
from playwright.sync_api import Page, expect

def test_my_feature(page: Page):
    page.goto("https://example.com")
    expect(page.locator("h1")).to_have_text("Example Domain")
```

See the [Playwright for Python docs](https://playwright.dev/python/) and [pytest-playwright docs](https://playwright.dev/python/docs/test-runners) for more.

## Project Structure

```
playwright-tests/
├── .github/workflows/
│   └── tests.yml               # GitHub Actions CI workflow
├── pyproject.toml              # Project config and dependencies
├── pytest.ini                  # pytest defaults (browser=chromium)
├── tests/
│   ├── test_example.py         # Basic tests against playwright.dev
│   ├── test_setup_verify.py    # Setup verification against example.com
│   └── test_e2e.py             # End-to-end multi-step tests
```
