# Product Requirements Document (PRD)
## Classificador de Leitura de Livros

### 1. Visão Geral
Este documento especifica os requisitos funcionais e as regras de negócio para o **Classificador de Leitura de Livros**, desenvolvido como parte do trabalho prático da disciplina de Qualidade e Teste de Software (QTS). O sistema recebe os dados de um livro lido pelo usuário (título, número de páginas e nível de complexidade) e devolve uma **classificação de leitura** ("Leitura Leve", "Leitura Moderada" ou "Leitura Densa"), além de um **tempo estimado de leitura em dias**, calculado de forma determinística a partir da velocidade média de leitura ajustada pela complexidade.

---

### 2. Regras de Negócio (BR - Business Rules)

#### **BR01: Validação do Número de Páginas**
- O campo `paginas` deve ser um número **inteiro** estritamente no intervalo fechado entre **1 e 5000**.
- Caso o valor esteja fora desse intervalo, o sistema deve lançar uma exceção do tipo `ValueError`.
- Caso a entrada fornecida não seja um inteiro válido (ex: strings, booleanos ou nulos), o sistema deve lançar uma exceção do tipo `TypeError`.

#### **BR02: Validação da Complexidade**
- O campo `complexidade` deve ser um número **inteiro** estritamente no intervalo fechado entre **1 e 5** (sendo 1 = leitura muito fácil e 5 = leitura muito densa).
- Caso o valor esteja fora desse intervalo, o sistema deve lançar uma exceção do tipo `ValueError`.
- Caso a entrada fornecida não seja um inteiro válido (ex: strings, booleanos ou nulos), o sistema deve lançar uma exceção do tipo `TypeError`.

#### **BR03: Cálculo do Tempo Estimado de Leitura**
- A velocidade base de leitura é de **50 páginas por dia** (`VELOCIDADE_BASE = 50`).
- A velocidade efetiva é ajustada pela complexidade:
  $$\text{páginas por dia} = \frac{\text{VELOCIDADE\_BASE}}{\text{complexidade}}$$
- O tempo estimado em dias é calculado por:
  $$\text{tempo\_estimado\_dias} = \left\lceil \frac{\text{paginas}}{\text{páginas por dia}} \right\rceil$$
- O resultado é sempre um inteiro (arredondado para cima).

#### **BR04: Classificação de Leitura**
Com base no **peso de leitura** definido como `peso = paginas × complexidade`, o sistema classifica a obra em:
1. **Leitura Leve:** Aplicado quando `peso ≤ 300`
2. **Leitura Moderada:** Aplicado quando `300 < peso ≤ 800`
3. **Leitura Densa:** Aplicado quando `peso > 800`

#### **BR05: Resposta Consolidada da API**
- O endpoint `POST /api/classificar` deve retornar um JSON com os campos:
  - `titulo` (string)
  - `paginas` (int)
  - `complexidade` (int)
  - `peso_leitura` (int)
  - `tempo_estimado_dias` (int)
  - `classificacao` (string)
- Entradas inválidas devem ser rejeitadas pelo Pydantic com status HTTP **422 (Unprocessable Entity)**.

---

### 3. Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Página HTML da interface web (formulário de classificação) |
| `POST` | `/api/classificar` | Recebe os dados do livro e retorna a classificação consolidada |

**Contrato do `POST /api/classificar`:**

```json
// Request
{
  "titulo": "Dom Casmurro",
  "paginas": 256,
  "complexidade": 3
}

// Response 200 OK
{
  "titulo": "Dom Casmurro",
  "paginas": 256,
  "complexidade": 3,
  "peso_leitura": 768,
  "tempo_estimado_dias": 16,
  "classificacao": "Leitura Moderada"
}