from Autor import Autor

class ListaEncadeadaAutor:
    def __init__(self):
        self.inicio = None

    def adicionar_autor(self, nome, nacionalidade):
        """ Adiciona um novo autor à lista em ordem alfabética pelo nome. """
        novo_autor = Autor(nome, nacionalidade)

        # Se a lista está vazia ou o novo autor vem antes do primeiro
        if self.inicio is None or novo_autor.nome.lower() < self.inicio.nome.lower():
            novo_autor.prox = self.inicio
            self.inicio = novo_autor
        else:
            # Procura a posição correta para inserir
            atual = self.inicio
            while atual.prox and novo_autor.nome.lower() > atual.prox.nome.lower():
                atual = atual.prox
            novo_autor.prox = atual.prox
            atual.prox = novo_autor
        print(f"Autor '{nome}' adicionado com sucesso.")

    def imprimir(self):
        """ Imprime todos os autores na lista. """
        print("\n--- Lista de Autores (Ordenada) ---")
        if self.inicio is None:
            print("Nenhum autor cadastrado.")
        else:
            aux = self.inicio
            while aux:
                print(f"- {aux}")
                aux = aux.prox
        print("------------------------------------")

    def buscar_autor(self, nome):
        """ Busca um autor pelo nome e retorna o objeto Autor. """
        aux = self.inicio
        while aux:
            if aux.nome.lower() == nome.lower():
                return aux
            aux = aux.prox
        return None
