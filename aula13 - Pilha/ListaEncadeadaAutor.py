from Autor import Autor

class ListaEncadeadaAutor():
    def __init__(self):
        self.inicio = None

    def adicionar_autor(self, autor):
        if self.inicio is None or autor.nome < self.inicio.nome:
            autor.prox = self.inicio
            self.inicio = autor
        else:
            atual = self.inicio
            while atual.prox and atual.prox.nome < autor.nome:
                atual = atual.prox
            autor.prox = atual.prox
            atual.prox = autor

    def imprimir(self):
        print("---------------------------------")
        if self.inicio is None:
            print( "Nenhum autor encontrado!" )
        else:
            aux = self.inicio
            while aux:
                print(aux.nome)
                aux = aux.prox

    def remover(self, nome):
        if self.inicio != None:
            removeu = False
            if self.inicio.nome == nome:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None:
                    if nome == aux.nome:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if removeu:
                    print("Elemento ", nome, " Removido!")
                else:
                    print("Elemento Não Encontrado!")
        self.imprimir()