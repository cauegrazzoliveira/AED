import os
from Fila import Fila

fila = Fila()
op = -1

while op != 0:
    os.system("cls")
    print("----------------------")
    print("1 - Adicionar na Fila")
    print("2 - Remover da Fila")
    print("3 - Imprimir Fila")
    print("0 - Sair")
    try:
        op = int(input("Digite sua opção: "))
        if op == 1:
            dado = input("Digite o valor que será imprimido na Fila: ")
            fila.add(dado)
        elif op == 2:
            fila.remover()
        elif op == 3:
            fila.imprimir()
        elif op != 0:
            print("Opção inválida!")
        input("Enter para continuar...")
    except:
        print("Opção inválida!")
        input("Enter para continuar...")
        continue