import random

vetor = [random.randint(1, 100) for _ in range(20)]
print("Vetor original:", vetor)

def buscaSeq(vetor, k):
    for i in range(len(vetor)):
        if vetor[i] == k:
            return i
    return -1 

def buscaBin(vetor, k):
    vetor.sort()  
    print("Vetor ordenado:", vetor)
    
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        centro = (inicio + fim) // 2
        if vetor[centro] == k:
            return centro
        elif k > vetor[centro]:
            inicio = centro + 1
        else:
            fim = centro - 1

    return -1  


numero = int(input("Digite um número para buscar: "))

pos_seq = buscaSeq(vetor, numero)
print(f"Busca Sequencial: posição {pos_seq}" if pos_seq != -1 else "Busca Sequencial: número não encontrado")

pos_bin = buscaBin(vetor, numero)
print(f"Busca Binária: posição {pos_bin}" if pos_bin != -1 else "Busca Binária: número não encontrado")
