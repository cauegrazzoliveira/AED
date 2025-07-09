"""
1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número do
apartamento, número da vaga de garagem e torre.
2) Este condomínio, não possui vagas de garagem para todos os apartamentos. Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha os métodos para adicionar
apartamentos na fila, retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.
3) Construa um menu de opções ao usuário, com as funcionalidades do algoritmo. 
Tente não enviar arquivos compactados."""
from Apartamento import Apartamento
from Torre import Torre
from FilaApartamento import FilaApartamento
import os

apartamento = Apartamento()
torre = Torre()
filaApartamento = FilaApartamento()
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
            filaApartamento().add()
        elif op == 2:
            filaApartamento.remover()
        elif op == 3:
            filaApartamento.imprimir()
        elif op != 0:
            print("Opção inválida!")
        input("Enter para continuar...")
    except:
        print("Opção inválida!")
        input("Enter para continuar...")
        continue