from Livro import Livro
from Autor import Autor

class PilhaLivro:
    def __init__(self):
        self.topo = None

    def add(self, titulo: str, autor: Autor, paginas: int):
        """ Adiciona um livro ao topo da pilha. """
        novo_livro = Livro(titulo, autor, paginas)
        novo_livro.prox = self.topo
        self.topo = novo_livro
        print(f"Livro '{titulo}' empilhado.")

    def deletar(self):
        """ Remove e retorna o livro do topo da pilha. """
        if self.topo is None:
            print("A pilha de livros está vazia!")
            return None
        livro_removido = self.topo
        self.topo = self.topo.prox
        print(f"Livro '{livro_removido.titulo}' removido da pilha.")
        return livro_removido

    def imprimir(self):
        """ Imprime todos os livros na pilha. """
        print("\n--- Pilha de Livros ---")
        if self.topo is None:
            print("Pilha vazia!")
        else:
            aux = self.topo
            while aux:
                print(f"- {aux}") # Usa o __str__ do Livro
                aux = aux.prox
        print("-----------------------")
