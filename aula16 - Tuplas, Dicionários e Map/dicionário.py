carro1 = {
    'modelo' : 'Gol',
    'ano' : 1990
}
carro2 = {
    'modelo' : 'Chevette',
    'ano' : 1992
}
carro3 = {
    'modelo' : 'Diplomata',
    'ano' : 1986
}

print(carro1['modelo'])
for chave in carro1.keys():
    print(chave)

print("--------------------------------------")

print(carro1['modelo'])
for chave, valor in carro1.items():
    print(chave, ":", valor)

frota = carro1, carro2

print("--------------------------------------")

print(frota)