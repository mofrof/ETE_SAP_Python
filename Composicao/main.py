from Produto import *
from Venda import *

p1 = Produto("macarrao", 10, 5)
p2 = Produto("feijao", 2.5, 5)

vendaEspecial = Venda("Zezinho", p1)
vendaEspecial.produto = p2

print(vendaEspecial.produto.nome)