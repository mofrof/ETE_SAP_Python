from Objetos.ProgramaTV import *


class Serie(ProgramaTV):

    def __init__ (self, nome, quantidadeTemporadas,
    anoLancamento,valorDeCompra):
        super().__init__(nome,anoLancamento,valorDeCompra)
        self.__quantidadeTemporadas = quantidadeTemporadas
            
    def exibirDados(self):
        super().exibirDados()
        print(f"Quantidade de temporadas: {self.__quantidadeTemporadas}")

    def venderSerie(self, valorSugerido):
        if (valorSugerido < 
        self.__valorDeCompra + 
        (self.__valorDeCompra * 0.2) ):
            print("Não vendo")
        else:
            self.disponivel = False