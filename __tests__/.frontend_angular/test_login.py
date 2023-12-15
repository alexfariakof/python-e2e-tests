"""Test e2e Create Account Angular."""
import re
from playwright.sync_api import Page, expect
from config.environments import get_config


local_config = get_config('local')
base_url = local_config['angular']


def test_has_title(page: Page):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto(base_url)

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesas Pessoais"))


def test_get_started_link(page: Page):
    """Function Get Started Link."""

    # Arrange and Act
    page.goto(base_url)

    # Click the get started link.
    page.wait_for_selector("button:has-text('Entrar')")
    page.click("button:has-text('Entrar')")

    # Wait for the navigation to complete.
    page.wait_for_url(f"{base_url}/dashboard", timeout=10000)

    # Assert
    assert page.url == f"{base_url}/dashboard"
    expect(page.locator("app-root")).to_be_visible()
    expect(page.locator("app-dashboard")).to_be_visible()
    expect(page.locator("app-layout")).to_be_visible()
