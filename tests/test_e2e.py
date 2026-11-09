import pytest
from playwright.sync_api import Page, expect
from tests.pages.reading_page import ReadingPage


@pytest.mark.e2e
def test_pagina_inicial_carrega(page: Page, live_server: str):
    po = ReadingPage(page, base_url=live_server)
    po.goto()
    expect(po.titulo_input).to_be_visible()
    expect(po.paginas_input).to_be_visible()
    expect(po.complexidade_input).to_be_visible()
    expect(po.botao).to_be_visible()


@pytest.mark.e2e
def test_fluxo_classificacao_leitura_leve(page: Page, live_server: str):
    po = ReadingPage(page, base_url=live_server)
    po.goto()
    po.preencher("Livro Curto", "100", "2")
    po.classificar()
    # Se você renderizar o resultado na página, valide aqui:
    # expect(page.get_by_text("Leitura Leve")).to_be_visible()