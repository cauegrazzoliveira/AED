from ListaEncadeada import ListaEncadeada
lista = ListaEncadeada()
lista.imprimir()
lista.addNoInicio("Adalto")
lista.addNoInicio("Abel")
lista.addNoFim("Cleber")

lista.remover("João")
print("#######################################################")
lista.removerDoFim()
print("#######################################################")
lista.removerDoInicio()