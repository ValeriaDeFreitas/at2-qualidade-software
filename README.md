
---

## 📄 `README.md`

```markdown
# Classificador de Leitura de Livros

Trabalho prático individual desenvolvido para a disciplina de Qualidade e Teste de Software (QTS), focado em engenharia de testes de integração, E2E, acessibilidade, carga e governança de IA.

## 📌 Sobre o Domínio

O sistema recebe os dados de um livro (título, número de páginas e nível de complexidade) e devolve:

- **Tempo estimado de leitura em dias**, calculado a partir da velocidade base de 50 páginas/dia, ajustada pela complexidade.
- **Classificação de leitura** com base no "peso de leitura" (`paginas × complexidade`):
  - `peso ≤ 300` → **Leitura Leve**
  - `300 < peso ≤ 800` → **Leitura Moderada**
  - `peso > 800` → **Leitura Densa**

Validações defensivas garantem o lançamento de exceções para entradas inválidas (páginas fora de 1–5000, complexidade fora de 1–5, tipos não-inteiros).

---

## 🛠️ Requisitos Técnicos

- **Python** ≥ 3.12
- **Gerenciador de Dependências:** `uv`
- **Stack:** FastAPI, Pydantic, pytest, pytest-mock, Faker, Playwright, Axe-core, Locust

---

## 🚀 Instruções de Execução

### 1. Clonar o repositório e configurar o ambiente

Certifique-se de ter o `uv` instalado. Na raiz do projeto:

```bash
# Sincronizar dependências e criar ambiente virtual
uv sync

# Instalar o navegador do Playwright
uv run playwright install chromium