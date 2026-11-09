from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from atividade_qts1.reading import ReadingEvaluator

app = FastAPI(
    title="Classificador de Leitura - QTS",
    description="API e interface web para classificar a leitura de um livro",
    version="2.0.0",
)


class LivroSchema(BaseModel):
    titulo: str = Field(..., min_length=2)
    paginas: int = Field(..., ge=1, le=5000)
    complexidade: int = Field(..., ge=1, le=5)


def calcular_classificacao(paginas: int, complexidade: int) -> dict:
    """Função isolada para permitir mock no teste de integração."""
    return ReadingEvaluator.avaliar(paginas, complexidade)


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Classificador de Leitura - QTS</title>
        <style>
            body { font-family: system-ui, sans-serif; background: #f3f4f6; padding: 30px; color: #1f2937; }
            .card { background: white; padding: 24px; border-radius: 8px; max-width: 480px; margin: auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .campo-grupo { margin-bottom: 16px; }
            label { display: block; margin-bottom: 6px; font-weight: bold; }
            input, select { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
            button { background-color: #2563eb; color: white; border: none; padding: 12px; width: 100%; border-radius: 4px; font-weight: bold; cursor: pointer; }
            button:focus, input:focus, select:focus { outline: 2px solid #2563eb; }
            #resultado { margin-top: 15px; font-weight: bold; color: #059669; }
        </style>
    </head>
    <body>
        <main class="card">
            <h1>Classificador de Leitura</h1>
            <p>Informe os dados do livro para descobrir sua classificação de leitura.</p>
            <form id="form-livro">
                <div class="campo-grupo">
                    <label for="titulo">Título do Livro</label>
                    <input type="text" id="titulo" name="titulo" placeholder="Ex: Dom Casmurro" required>
                </div>
                <div class="campo-grupo">
                    <label for="paginas">Número de Páginas</label>
                    <input type="number" id="paginas" name="paginas" min="1" max="5000" required>
                </div>
                <div class="campo-grupo">
                    <label for="complexidade">Complexidade (1 a 5)</label>
                    <input type="number" id="complexidade" name="complexidade" min="1" max="5" required>
                </div>
                <button type="submit" id="btn-classificar">Classificar Leitura</button>
            </form>
            <div id="resultado" aria-live="polite"></div>
        </main>
        <script>
            document.getElementById("form-livro").addEventListener("submit", async (e) => {
                e.preventDefault();
                const payload = {
                    titulo: document.getElementById("titulo").value,
                    paginas: parseInt(document.getElementById("paginas").value, 10),
                    complexidade: parseInt(document.getElementById("complexidade").value, 10),
                };
                const resp = await fetch("/api/classificar", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(payload),
                });
                const data = await resp.json();
                document.getElementById("resultado").textContent =
                    `Classificação: ${data.classificacao} — ${data.tempo_estimado_dias} dias estimados`;
            });
        </script>
    </body>
    </html>
    """


@app.post("/api/classificar", status_code=status.HTTP_200_OK)
def classificar_livro(livro: LivroSchema):
    resultado = calcular_classificacao(livro.paginas, livro.complexidade)
    return {
        "titulo": livro.titulo,
        **resultado,
    }