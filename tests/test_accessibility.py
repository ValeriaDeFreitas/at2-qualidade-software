import pytest
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe


@pytest.mark.accessibility
def test_wcag_acessibilidade(page: Page, live_server: str):
    page.goto(live_server)
    axe = Axe()
    results = axe.run(page)
    assert len(results.violations) == 0, results.violations


@pytest.mark.accessibility
def test_navegacao_por_teclado(page: Page, live_server: str):
    page.goto(live_server)
    page.keyboard.press("Tab")
    page.get_by_label("Título do Livro").to_be_focused()

    page.keyboard.press("Tab")
    page.get_by_label("Número de Páginas").to_be_focused()