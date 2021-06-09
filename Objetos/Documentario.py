from Objetos.ProgramaTV import *

class Documentario(ProgramaTV):
    
    def __init__(self, quantEp, nome, anoLancamento, valorDeCompra):
        super().__init__(nome,anoLancamento,valorDeCompra)
        self.__quantEp = quantEp

    def exibirDados(self):
        super().exibirDados()
        print(f"Quantidade de epsodios: R$ {self.__quantEp}")
        