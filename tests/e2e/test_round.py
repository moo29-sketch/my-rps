"""RPS-001: play and replay using Chromium and the actual HTTP server."""

# pytest injects the supplied fixtures by name.
# pylint: disable=redefined-outer-name,missing-function-docstring

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_browser_round_and_replay(page: Page, live_server, monkeypatch):
    """Winning first, then losing proves a new choice starts another round."""
    computer_moves = iter(("scissors", "paper"))
    monkeypatch.setattr(web.random, "choice", lambda _moves: next(computer_moves))

    page.goto(live_server)
    expect(page.get_by_role("button", name="Rock", exact=True)).to_be_visible()
    expect(page.get_by_role("status")).to_have_count(0)

    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.locator('[data-outcome="win"]')).to_be_visible()
    expect(page.get_by_role("heading", name="You win!")).to_be_visible()
    choices = page.get_by_label("This round’s choices")
    expect(choices).to_contain_text("Rock")
    expect(choices).to_contain_text("Scissors")

    # A second click submits an independent round through the same real server.
    page.get_by_role("button", name="Rock", exact=True).click()
    expect(page.locator('[data-outcome="lose"]')).to_be_visible()
    expect(page.get_by_role("heading", name="Computer wins")).to_be_visible()
    choices = page.get_by_label("This round’s choices")
    expect(choices).to_contain_text("Rock")
    expect(choices).to_contain_text("Paper")
    expect(page.locator("[data-outcome]")).to_have_count(1)
