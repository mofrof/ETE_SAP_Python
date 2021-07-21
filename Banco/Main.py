from ContaPoupanca import *
from ContaCorrente import *
from Conta import *
from Cliente import *


cliente = Cliente("Renato", "Professor")
contaZezinho = ContaCorrente(1234, 15, cliente)

contaZezinho.cliente.profissao


contaZezinho.Saque(10)




