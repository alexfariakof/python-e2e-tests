"""Module Test Example functions."""
import re
from playwright.sync_api import Page, expect
from config.environment import BASE_URL


def test_has_title(page: Page):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto(BASE_URL)

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesas Pessoais"))


def test_get_started_link(page: Page):
    """Function Get Started Link."""

    # Arrange and Act
    page.goto(BASE_URL)

    # Click the get started link.
    page.wait_for_selector("button:has-text('Entrar')")
    page.click("button:has-text('Entrar')")

    # Wait for the navigation to complete.
    page.wait_for_url(f"{BASE_URL}/dashboard", timeout=10000)

    # Assert
    assert page.url == f"{BASE_URL}/dashboard"
    expect(page.locator("app-root")).to_be_visible()
    expect(page.locator("app-dashboard")).to_be_visible()
    expect(page.locator("app-layout")).to_be_visible()
