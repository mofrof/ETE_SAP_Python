from Objetos.ProgramaTV import *

class Filme(ProgramaTV):
    def __init__(self, nome,anoLancamento,
    disponivel, valorDeCompra):
            super().__init__(nome,anoLancamento,valorDeCompra)
            self.__disponivel = disponivel
       

    def venderSerie(self, valorSugerido):
        if (valorSugerido < 
        self.__valorDeCompra + 
        (self.__valorDeCompra * 0.1) ):
            print("Não vendo")
        else:
            self.disponivel = False
    
    def venderFilme(self, valorSugerido):
        if (valorSugerido < 
        self.__valorDeCompra + 
        (self.__valorDeCompra * 0.2) ):
            print("Não vendo")
        else:
            self.disponivel = False
