from PilhaLivro import PilhaLivro
from ListaEncadeadaAutor import ListaEncadeadaAutor

def menu_livros(pilha, fila):
    while True:
        print("\n--- Menu Livros ---")
        print("1. Adicionar Livro na Pilha")
        print("2. Remover Livro da Pilha")
        print("3. Imprimir Pilha de Livros")
        print("4. Adicionar Livro na Fila")
        print("5. Remover Livro da Fila")
        print("6. Imprimir Fila de Livros")
        print("7. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            paginas = int(input("Número de páginas: "))
            pilha.push(titulo, autor, paginas)
        elif escolha == '2':
            pilha.pop()
        elif escolha == '3':
            pilha.imprimir()
        elif escolha == '4':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            paginas = int(input("Número de páginas: "))
            fila.enqueue(titulo, autor, paginas)
        elif escolha == '5':
            fila.dequeue()
        elif escolha == '6':
            fila.imprimir()
        elif escolha == '7':
            break
        else:
            print("Opção inválida!")

def menu_autores(lista_autores):
    while True:
        print("\n--- Menu Autores ---")
        print("1. Adicionar Autor no Início")
        print("2. Adicionar Autor no Fim")
        print("3. Remover Autor do Início")
        print("4. Remover Autor do Fim")
        print("5. Remover Autor por Nome")
        print("6. Imprimir Lista de Autores")
        print("7. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            lista_autores.addNoInicio(nome, nacionalidade)
        elif escolha == '2':
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            lista_autores.addNoFim(nome, nacionalidade)
        elif escolha == '3':
            lista_autores.removerDoInicio()
        elif escolha == '4':
            lista_autores.removerDoFim()
        elif escolha == '5':
            nome = input("Nome do autor a ser removido: ")
            lista_autores.remover(nome)
        elif escolha == '6':
            lista_autores.imprimir()
        elif escolha == '7':
            break
        else:
            print("Opção inválida!")

def main():
    pilha_livros = PilhaLivro()
    fila_livros = FilaLivro()
    lista_autores = ListaEncadeadaAutor()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Autores")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_livros(pilha_livros, fila_livros)
        elif escolha == '2':
            menu_autores(lista_autores)
        elif escolha == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
