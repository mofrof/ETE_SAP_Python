from Objetos.ProgramaTV import *


class Serie(ProgramaTV):

    def __init__ (self, nome, quantidadeTemporadas,
    anoLancamento, disponivel,valorDeCompra):
        super().__init__(nome,anoLancamento,valorDeCompra)
        self.__quantidadeTemporadas = quantidadeTemporadas
        self.__disponivel = disponivel
            
    def venderSerie(self, valorSugerido):
        if (valorSugerido < 
        self.__valorDeCompra + 
        (self.__valorDeCompra * 0.2) ):
            print("Não vendo")
        else:
            self.disponivel = False