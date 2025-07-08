from Autor import Autor

class ListaEncadeadaAutor:
    def __init__(self):
        self.inicio = None

    def addNoInicio(self, nome, nacionalidade):
        """ Adiciona um autor no início da lista. """
        novo_autor = Autor(nome, nacionalidade)
        novo_autor.prox = self.inicio
        self.inicio = novo_autor
        print(f"Autor '{nome}' adicionado no início.")

    def addNoFim(self, nome, nacionalidade):
        """ Adiciona um autor no fim da lista. """
        novo_autor = Autor(nome, nacionalidade)
        if self.inicio is None:
            self.inicio = novo_autor
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = novo_autor
        print(f"Autor '{nome}' adicionado no fim.")

    def imprimir(self):
        """ Imprime todos os autores na lista. """
        print("--- Lista de Autores ---")
        if self.inicio is None:
            print("Lista de autores está vazia!")
        else:
            aux = self.inicio
            while aux:
                print(f"Nome: {aux.nome}, Nacionalidade: {aux.nacionalidade}")
                aux = aux.prox
        print("------------------------")

    def removerDoInicio(self):
        """ Remove o autor do início da lista. """
        if self.inicio is None:
            print("Lista de autores está vazia!")
            return
        autor_removido = self.inicio.nome
        self.inicio = self.inicio.prox
        print(f"Autor '{autor_removido}' removido do início.")

    def removerDoFim(self):
        """ Remove o autor do fim da lista. """
        if self.inicio is None:
            print("Lista de autores está vazia!")
            return
        if self.inicio.prox is None:
            autor_removido = self.inicio.nome
            self.inicio = None
            print(f"Autor '{autor_removido}' removido.")
            return

        ant = self.inicio
        aux = self.inicio.prox
        while aux.prox:
            ant = aux
            aux = aux.prox
        autor_removido = aux.nome
        ant.prox = None
        print(f"Autor '{autor_removido}' removido do fim.")

    def remover(self, nome):
        """ Remove um autor específico pelo nome. """
        if self.inicio is None:
            print("Lista de autores está vazia!")
            return

        if self.inicio.nome.lower() == nome.lower():
            self.removerDoInicio()
            return

        ant = self.inicio
        aux = self.inicio.prox
        while aux:
            if aux.nome.lower() == nome.lower():
                ant.prox = aux.prox
                print(f"Autor '{aux.nome}' removido!")
                return
            ant = aux
            aux = aux.prox
        print(f"Autor '{nome}' não encontrado!")
