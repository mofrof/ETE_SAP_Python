from Conta import *

class ContaCorrente(Conta):
    
    def __init__ (self, numero, saldo, cliente):
        super().__init__(numero, saldo)
        self.cliente = cliente

    def Saque(self, valor):
        print("classe filha")
        self.saldo -= valor
