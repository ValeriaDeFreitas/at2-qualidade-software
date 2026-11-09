from playwright.sync_api import Page, expect


class ReadingPage:
    URL = "http://127.0.0.1:8000"

    def __init__(self, page: Page):
        self.page = page
        self.titulo_input = page.get_by_label("Título do Livro")
        self.paginas_input = page.get_by_label("Número de Páginas")
        self.complexidade_input = page.get_by_label("Complexidade (1 a 5)")
        self.botao = page.get_by_role("button", name="Classificar Leitura")

    def goto(self):
        self.page.goto(self.URL)
        expect(self.page).to_have_title("Classificador de Leitura - QTS")

    def preencher(self, titulo: str, paginas: str, complexidade: str):
        self.titulo_input.fill(titulo)
        self.paginas_input.fill(paginas)
        self.complexidade_input.fill(complexidade)

    def classificar(self):
        self.botao.click()
        