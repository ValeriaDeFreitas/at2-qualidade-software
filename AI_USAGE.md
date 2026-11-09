
---

## 📄 `AI_USAGE.md`

```markdown
# Relatório de Transparência de Uso de Inteligência Artificial (AI_USAGE.md)

Este documento descreve de forma transparente o papel das ferramentas de Inteligência Artificial no desenvolvimento deste trabalho prático para a disciplina de Qualidade e Teste de Software (QTS).

## 1. Ferramentas Utilizadas
- **Assistente de IA:** Google Gemini.
- **Ambiente de Desenvolvimento (IDE):** Visual Studio Code.
- **Gerenciador de Dependências:** `uv` (Python 3.12+).

## 2. Como a IA foi Empregada
A Inteligência Artificial (Google Gemini) foi utilizada como suporte técnico nas seguintes etapas:

- **Especificação de Requisitos (PRD):** Auxílio na estruturação inicial das regras de negócio determinísticas para o **Classificador de Leitura de Livros** (cálculo do tempo estimado de leitura a partir de páginas e complexidade, e definição das faixas de classificação com base no peso de leitura).
- **Implementação do Domínio (SUT):** Apoio na escrita do código Python do módulo `ReadingEvaluator`, aplicando boas práticas de tipagem estática (*Type Hints*), arredondamento determinístico com `math.ceil` e tratamento defensivo de exceções (`ValueError` e `TypeError`).
- **Suíte de Testes Unitários:** Geração orientada de casos de teste parametrizados aplicando técnicas de caixa branca e preta, nomeadamente **Particionamento de Equivalência (EP)**, **Análise do Valor Limite (BVA)** e **Error Guessing** sobre os limites de páginas (1–5000) e complexidade (1–5).
- **Testes de Integração e E2E:** Apoio na estruturação das factories com `Faker("pt_BR")`, no uso de `mocker.patch` para isolar a função `calcular_classificacao`, e no padrão **Page Object Model (POM)** para os testes com Playwright.
- **Auditoria de Acessibilidade:** Sugestão de estrutura HTML acessível (labels associados, `aria-live` para o resultado) e do teste com Axe-core para conformidade WCAG 2.1 AA.

## 3. Auditoria e Validação Humana
Todo o código gerado pelo Gemini foi rigorosamente auditado e validado pelo autor do projeto:

1. **Revisão Crítica:** O código foi verificado linha por linha para garantir conformidade com os padrões da linguagem e com as regras de negócio exigidas no PRD.
2. **Execução de Testes:** A suíte completa foi validada diretamente no terminal utilizando o framework `pytest`:

   ```bash
   uv run pytest -v