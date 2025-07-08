from Livro import Livro

class PilhaLivro:
    def __init__(self):
        self.topo = None

    def push(self, titulo, autor, paginas):
        """ Adiciona um livro ao topo da pilha. """
        novo_livro = Livro(titulo, autor, paginas)
        novo_livro.prox = self.topo
        self.topo = novo_livro
        print(f"Livro '{titulo}' adicionado à pilha.")

    def pop(self):
        """ Remove o livro do topo da pilha. """
        if self.topo is None:
            print("A pilha de livros está vazia!")
            return None
        livro_removido = self.topo
        self.topo = self.topo.prox
        print(f"Livro '{livro_removido.titulo}' removido da pilha.")
        return livro_removido

    def imprimir(self):
        """ Imprime todos os livros na pilha, do topo para a base. """
        print("--- Pilha de Livros ---")
        if self.topo is None:
            print("Pilha vazia!")
        else:
            aux = self.topo
            while aux:
                print(f"Título: {aux.titulo}, Autor: {aux.autor}, Páginas: {aux.paginas}")
                aux = aux.prox
        print("-----------------------")
