from abc import ABC, abstractmethod

class Produto:
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria

    def getInformacaoes():
        pass

    @abstractmethod
    def cadastrar():
        pass