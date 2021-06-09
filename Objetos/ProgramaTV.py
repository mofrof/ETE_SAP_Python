class ProgramaTV:

    def __init__(self, nome, anoLancamento,valorDeCompra,):
        self.nome = nome.capitalize()
        self.anoLancamento = anoLancamento
        self.valorDeCompra = valorDeCompra

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Ano lancamento: {self.anoLancamento}")
        print(f"Valor de compra: R$ {self.valorDeCompra}")

    def vender(self,valorSugerido):
        if (valorSugerido < 
        self.valorDeCompra + 
        (self.valorDeCompra * 0.2) ):
            print("Não pode vendo")
        else:
            print("Pode vender")