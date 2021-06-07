class ContaCorrente:

    def __init__(self, numeroConta, nomeTitular, saldo, chequeEspecial):
        self.__numeroConta = numeroConta
        self.__nomeTitular = nomeTitular.capitalize()
        self.__saldo = saldo
        self.__chequeEspecial = chequeEspecial
    
    @staticmethod   
    def numeroDoBanco():
        return 321

    @property
    def nomeTitular(self):
        print("Metodo GET")
        return self.__nomeTitular

    @nomeTitular.setter
    def nomeTitular(self,novoNome):
        print("Metodo SET")
        self.__nomeTitular = novoNome.capitalize()

    def exbiDados(self):
        print(f"Número da conta: {self.__numeroConta}")
        print(f"Nome do Titular: {self.__nomeTitular}")
        print(f"Saldo: {self.__saldo}")
        print(f"Cheque Especial: {self.__chequeEspecial}")
    
    def __possuiLimiteParaSaque(self,valorDoSaque):
        return valorDoSaque <= self.__saldo + self.__chequeEspecial

    def saque(self, valorDoSaque):
        if(self.__possuiLimiteParaSaque(valorDoSaque)):
            if(valorDoSaque <= self.__saldo):
                self.__saldo = self.__saldo - valorDoSaque
            else:
                valorDoSaque = valorDoSaque - self.__saldo
                self.__saldo = 0
                self.__chequeEspecial = self.__chequeEspecial - valorDoSaque

            print("Saque realizado com sucesso!")
        else:
            print("Você não tem limite suficiente para o saque!") 