"""Test e2e Test Login in Frontend React"""
import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page, config):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto(config)

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesas"))


def test_get_started_link(page: Page, config):
    """Function Get Started Link."""

    # Arrange and Act
    page.goto(config)

    # Click the get started link.
    page.wait_for_selector("button:has-text('Entrar')")
    page.click("button:has-text('Entrar')")

    # Wait for the navigation to complete.
    page.wait_for_url(f"{config}/pagina-inicial", timeout=10000)

    # Assert
    assert page.url == f"{config}/pagina-inicial"
    expect(page.locator("body")).to_be_visible()
    expect(page.locator("#root")).to_be_visible()
    expect(page.locator("canvas")).to_be_visible()
