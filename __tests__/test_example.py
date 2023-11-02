"""Module Test Example functions."""
import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto("http://alexfariakof.com:3000")

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesas Pessoais"))
