from Objetos.ProgramaTV import *

class Documentario(ProgramaTV):
    
    def __init__(self, quantEp, nome, anoLancamento, valorDeCompra):
        super().__init__(nome,anoLancamento,valorDeCompra)
        self.__quantEp = quantEp

    def exibirDados(self):
        super().exibirDados()
        print(f"Quantidade de epsodios: R$ {self.__quantEp}")
        
    def venderDocumentario(self, valorSugerido):
        if (valorSugerido < 
        self.__valorDeCompra + 
        (self.__valorDeCompra * 0.2) ):
            print("Não vendo")
        else:
            self.disponivel = False