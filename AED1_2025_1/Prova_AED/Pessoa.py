from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome, cpf):
        self.id = 1
        self.nome = nome
        self._cpf = cpf

    @abstractmethod
    def marcarPresença(self):
        pass
        
    def set_cpf(self):
        return self._cpf
   
    @abstractmethod
    def matricular(self):
        pass

    def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + str(self._cpf)
    
