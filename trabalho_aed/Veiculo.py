from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    @abstractmethod
    def exibir_dados(self):
        pass

    def __str__(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}"
