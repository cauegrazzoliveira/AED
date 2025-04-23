from Pessoa import Pessoa
from Produto import Produto
from Cidade import Cidade
from Pedido import Pedido

c1 = Cidade()
c2 = Cidade("Porto Alegre")

p1 = Pessoa("João")
p2 = Pessoa("Maria" , cid = c1)

prod01 = Produto("Coca-cola", 9.99)
prod02 = Produto("Pepsi", qtd = 50)
prod03 = Produto("Fanta", 17.85, 30)

ped = Pedido(cliente = p2)
ped.addProd( prod02)
ped.addProd( prod03)

print(ped)



