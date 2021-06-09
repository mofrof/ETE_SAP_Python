from Objetos.ProgramaTV import *


class Serie(ProgramaTV):

    def __init__ (self, nome, quantidadeTemporadas,
    anoLancamento,valorDeCompra):
        super().__init__(nome,anoLancamento,valorDeCompra)
        self.__quantidadeTemporadas = quantidadeTemporadas
            
    def exibirDados(self):
        super().exibirDados()
        print(f"Quantidade de temporadas: {self.__quantidadeTemporadas}")