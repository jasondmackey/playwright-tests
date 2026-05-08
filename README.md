# Playwright Tests

Browser-based automated testing with [Playwright](https://playwright.dev/) and pytest.

## Prerequisites

- Python 3.11+
- pip

## Setup

```sh
pip install -e .
playwright install chromium
```

## Running Tests

```sh
# Run all tests (headless)
pytest

# Run with visible browser
pytest --headed

# Run a specific test file
pytest tests/test_setup_verify.py

# Verbose output
pytest -v
```

## Project Structure

```
playwright-tests/
├── pyproject.toml          # Project config and dependencies
├── pytest.ini              # pytest defaults (browser=chromium)
├── tests/
│   ├── test_example.py         # Example tests against playwright.dev
│   └── test_setup_verify.py    # Setup verification against example.com
```
