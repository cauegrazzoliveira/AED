from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula = None, nome = None, cpf = None):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    def __str__(self):
        return super().__str__() + "\nMatrícula: " + str(self.__matricula)
    
    def marcarPresença(self):
        presenca = input("Presença do aluno: ")
        return presenca

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self):
        return self.__matricula

    def imprimir(self):
        print(self)

    def matricular(self):
        self.nome = input("Digite o nome do aluno: ")
        self._cpf = input("Digite o cpf: ")
        self.__matricula = input("Digite a matrícula: ")
        