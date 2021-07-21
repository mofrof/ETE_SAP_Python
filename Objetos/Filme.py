from Objetos.ProgramaTV import *

class Filme(ProgramaTV):
    def __init__(self, nome, anoLancamento,
                 disponivel, valorDeCompra):
        super().__init__(nome, anoLancamento, valorDeCompra)
        self.disponivel = disponivel

    def exibirDados(self):
        super().exibirDados()
        print("eu sou o texto da classe filme")
