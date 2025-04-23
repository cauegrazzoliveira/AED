from Cidade import Cidade

class Pessoa:
    def __init__(self, nome, cpf = None, cid = Cidade("Itati")):
        self.id = None
        self.nome = nome
        self.cpf = cpf
        self.cidade = cid

    def __str__(self):
        txt = f"Pessoa: " + self.nome
        txt += f"\nCPF: " + str(self.cpf)
        txt += f"\nCidade: " + str(self.cidade)
        return txt
        
        
        

