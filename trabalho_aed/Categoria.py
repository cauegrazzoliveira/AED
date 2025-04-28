from abc import ABC, abstractmethod

class Categoria(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def descricao_categoria(self):
        pass

    def __str__(self):
        return f"Categoria: {self.nome}"

class CategoriaConcreta(Categoria):
    def descricao_categoria(self):
        return f"Descrição da categoria {self.nome}"
