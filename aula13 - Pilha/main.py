from PilhaLivro import PilhaLivro
from ListaEncadeadaAutor import ListaEncadeadaAutor

def main():
    pilha_livros = PilhaLivro()
    lista_autores = ListaEncadeadaAutor()

    # Dados de exemplo para facilitar o teste
    lista_autores.adicionar_autor("George Orwell", "Britânico")
    lista_autores.adicionar_autor("J.R.R. Tolkien", "Britânico")
    lista_autores.adicionar_autor("Machado de Assis", "Brasileiro")


    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Adicionar Livro na Pilha")
        print("2. Remover Livro da Pilha")
        print("3. Imprimir Pilha de Livros")
        print("4. Adicionar Autor")
        print("5. Imprimir Lista de Autores")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1': # Adicionar Livro
            titulo = input("Digite o título do livro: ")
            nome_autor = input("Digite o nome do autor: ")

            autor = lista_autores.buscar_autor(nome_autor)
            if autor is None:
                print(f"Autor '{nome_autor}' não encontrado.")
                add_novo = input("Deseja adicioná-lo agora? (s/n): ").lower()
                if add_novo == 's':
                    nacionalidade = input(f"Digite a nacionalidade de {nome_autor}: ")
                    lista_autores.adicionar_autor(nome_autor, nacionalidade)
                    autor = lista_autores.buscar_autor(nome_autor) # Busca novamente após adicionar
                else:
                    print("Operação cancelada. O livro não foi adicionado.")
                    continue

            if autor:
                try:
                    paginas = int(input("Digite o número de páginas: "))
                    pilha_livros.push(titulo, autor, paginas)
                except ValueError:
                    print("Número de páginas inválido. Operação cancelada.")

        elif escolha == '2': # Remover Livro
            pilha_livros.pop()

        elif escolha == '3': # Imprimir Pilha
            pilha_livros.imprimir()

        elif escolha == '4': # Adicionar Autor
            nome = input("Digite o nome do autor: ")
            nacionalidade = input("Digite a nacionalidade do autor: ")
            lista_autores.adicionar_autor(nome, nacionalidade)

        elif escolha == '5': # Imprimir Autores
            lista_autores.imprimir()

        elif escolha == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
