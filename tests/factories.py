from faker import Faker

fake = Faker("pt_BR")


class LivroFactory:
    @staticmethod
    def criar():
        return {
            "titulo": fake.sentence(nb_words=4).rstrip("."),
            "paginas": fake.random_int(min=50, max=1500),
            "complexidade": fake.random_int(min=1, max=5),
        }

    @staticmethod
    def criar_invalido():
        return {
            "titulo": fake.sentence(nb_words=3).rstrip("."),
            "paginas": 99999,  # fora do limite
            "complexidade": 9,
        }