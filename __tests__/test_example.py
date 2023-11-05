"""Module Test Example functions."""
import re
from playwright.sync_api import Page, expect
from config.environment import BASE_URL


def test_has_title(page: Page):
    """Function Test Has Title."""

    # Arrage and Act
    page.goto(BASE_URL)

    # Assert Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Despesa Pessoais"))
