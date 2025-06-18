class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.prox = None

    def add(self):
        while True:
            name = input("Digite o nome do autor")
            if name:
                self.nome = name
                break
            else: 
                print("Digite um nome válido!")
                continue
        while True:
            nac = input("Digite a nacionalidade do autor")
            if nac:
                self.nacionalidade = nac
                break
            else: 
                print("Digite uma nacionalidade válida!")
                continue
        

    def imprimir(self):
        print("---------------------------------")
        if self.inicio is None:
            print( "Lista Encadeada está vazia!" )
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.prox

    def remover(self, valor):
        if self.inicio != None:
            removeu = False
            if self.inicio.dado == valor:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux != None:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        #break
                    else:
                        ant = aux
                        aux = aux.prox
                if removeu:
                    print("Elemento ", valor, " Removido!")
                else:
                    print("Elemento Não Encontrado!")
        self.imprimir()