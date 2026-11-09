import pytest
from tests.factories import LivroFactory


@pytest.mark.integration
def test_classificar_livro_sucesso(client):
    """Testa a rota de classificação usando dados do Faker."""
    dados = LivroFactory.criar()
    response = client.post("/api/classificar", json=dados)

    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == dados["titulo"]
    assert "classificacao" in data
    assert "tempo_estimado_dias" in data
    assert "peso_leitura" in data


@pytest.mark.integration
def test_classificar_livro_com_mock(client, mocker):
    """Isola o cálculo com mocker.patch.

    Importante: patch no módulo *onde a função é usada*
    (atividade_qts1.main), não no módulo de origem.
    """
    mocker.patch(
        "atividade_qts1.main.calcular_classificacao",
        return_value={
            "paginas": 100,
            "complexidade": 2,
            "peso_leitura": 200,
            "tempo_estimado_dias": 4,
            "classificacao": "Leitura Leve",
        },
    )

    dados = LivroFactory.criar()
    response = client.post("/api/classificar", json=dados)

    assert response.status_code == 200
    data = response.json()
    assert data["classificacao"] == "Leitura Leve"
    assert data["tempo_estimado_dias"] == 4


@pytest.mark.integration
def test_classificar_livro_dados_invalidos(client):
    """Testa rejeição do Pydantic para páginas fora do intervalo."""
    dados_invalidos = {
        "titulo": "Livro Inválido",
        "paginas": 0,
        "complexidade": 3,
    }
    response = client.post("/api/classificar", json=dados_invalidos)
    assert response.status_code == 422