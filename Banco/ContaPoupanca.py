from Conta import *

class ContaPoupanca(Conta):
    def __init__(self,numero, saldo, juros):
        super().__init__( numero, saldo)
        self.juros = juros
    
    def __getValorRendimento(self):
        return self.saldo * self.juros

    def renderJuros(self):
        self.saldo += self.__getValorRendimento()