class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.prox = None

    def __str__(self):
        return f"Nome: {self.nome}, Nacionalidade: {self.nacionalidade}"
