import pytest
from atividade_qts1.reading import ReadingEvaluator


@pytest.mark.unit
@pytest.mark.parametrize(
    "paginas, complexidade, esperado",
    [
        (50, 1, 1),    # leve
        (100, 2, 4),
        (1000, 5, 100),
    ],
)
def test_calcular_tempo_estimado(paginas, complexidade, esperado):
    assert ReadingEvaluator.calcular_tempo_estimado(paginas, complexidade) == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "paginas, complexidade, esperado",
    [
        (10, 1, "Leitura Leve"),       # peso 10
        (100, 2, "Leitura Leve"),      # peso 200
        (100, 3, "Leitura Moderada"),  # peso 300
        (200, 4, "Leitura Moderada"),  # peso 800
        (200, 5, "Leitura Densa"),     # peso 1000
        (1000, 5, "Leitura Densa"),    # peso 5000
    ],
)
def test_classificar_leitura_limites(paginas, complexidade, esperado):
    assert ReadingEvaluator.classificar_leitura(paginas, complexidade) == esperado


@pytest.mark.unit
@pytest.mark.parametrize(
    "paginas, complexidade",
    [
        (0, 3),
        (5001, 3),
        (100, 0),
        (100, 6),
    ],
)
def test_error_guessing_fora_do_intervalo(paginas, complexidade):
    with pytest.raises(ValueError):
        ReadingEvaluator.calcular_tempo_estimado(paginas, complexidade)


@pytest.mark.unit
@pytest.mark.parametrize(
    "paginas, complexidade",
    [
        ("100", 3),
        (100, "3"),
        (None, 3),
        (100, None),
        (True, 3),
        (100, False),
    ],
)
def test_error_guessing_tipos_invalidos(paginas, complexidade):
    with pytest.raises(TypeError):
        ReadingEvaluator.calcular_tempo_estimado(paginas, complexidade)