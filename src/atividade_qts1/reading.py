import math


class ReadingEvaluator:
    VELOCIDADE_BASE = 50  

    @staticmethod
    def calcular_tempo_estimado(paginas: int, complexidade: int) -> int:
        if not isinstance(paginas, int) or isinstance(paginas, bool):
            raise TypeError("O número de páginas deve ser um inteiro.")
        if not isinstance(complexidade, int) or isinstance(complexidade, bool):
            raise TypeError("A complexidade deve ser um inteiro.")
        if not (1 <= paginas <= 5000):
            raise ValueError("O número de páginas deve estar entre 1 e 5000.")
        if not (1 <= complexidade <= 5):
            raise ValueError("A complexidade deve estar entre 1 e 5.")

        paginas_por_dia = ReadingEvaluator.VELOCIDADE_BASE / complexidade
        return math.ceil(paginas / paginas_por_dia)

    @staticmethod
    def classificar_leitura(paginas: int, complexidade: int) -> str:
        # Reutiliza validações
        ReadingEvaluator.calcular_tempo_estimado(paginas, complexidade)

        peso = paginas * complexidade
        if peso < 300:
            return "Leitura Leve"
        elif peso <= 800:
            return "Leitura Moderada"
        else:
            return "Leitura Densa"

    @staticmethod
    def avaliar(paginas: int, complexidade: int) -> dict:
        tempo = ReadingEvaluator.calcular_tempo_estimado(paginas, complexidade)
        classificacao = ReadingEvaluator.classificar_leitura(paginas, complexidade)
        return {
            "paginas": paginas,
            "complexidade": complexidade,
            "peso_leitura": paginas * complexidade,
            "tempo_estimado_dias": tempo,
            "classificacao": classificacao,
        }