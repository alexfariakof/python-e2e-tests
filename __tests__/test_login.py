"""Module Test Example functions."""
import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto("http://alexfariakof.com:3000")

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesas Pessoais"))


def test_get_started_link(page: Page):
    """Function Get Started Link."""

    # Arrange and Act
    page.goto("http://alexfariakof.com:3000")

    # Click the get started link.
    page.wait_for_selector("button:has-text('Entrar')")
    page.click("button:has-text('Entrar')")

    # Wait for the navigation to complete.
    page.wait_for_url("http://alexfariakof.com:3000/dashboard", timeout=10000)

    # Assert
    assert page.url == "http://alexfariakof.com:3000/dashboard"
    expect(page.locator("app-root")).to_be_visible()
    expect(page.locator("app-dashboard")).to_be_visible()
    expect(page.locator("app-layout")).to_be_visible()
