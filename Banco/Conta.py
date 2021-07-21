class Conta():
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo

    def __possuiSaldo(self, valor):
        if(self.__saldo >= valor):
            return True
        else:
            return False

    def Saque(self, valor):
        if(self.__possuiSaldo(valor)):
            self.__saldo -= valor
        else:
            print("Você é pobre!!")
# GET
    @property 
    def saldo(self):
        return self.__saldo

# SET
    @saldo.setter
    def saldo(self, novoSaldo):
        self.__saldo = novoSaldo