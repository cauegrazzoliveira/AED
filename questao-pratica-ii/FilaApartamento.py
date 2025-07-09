from Apartamento import Apartamento
class FilaApartamento:
    def __init__(self):
        self.inicio = None

    def add(self):
        nodo = Apartamento()
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir(self)
    
    def imprimir(self):
        print("--------------- Fila - FIFO -------------------")
        if self.inicio is None:
            print( "Fila está vazia!" )
        else:
            aux = self.inicio
            txt = ""
            while aux :
                txt += aux.vaga + " - "
                aux = aux.prox
            print(txt)

    def remover(self):
        if self.inicio is not None:
            elemento = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print("Apartamento ", elemento.numero, " removido!")
        self.imprimir()