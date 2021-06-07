class ProgramaTV:

    def __init__(self, nome, anoLancamento,valorDeCompra,):
        self.teste = "Carro do ovo"
        self.nome = nome.capitalize()
        self.anoLancamento = anoLancamento
        self.valorDeCompra = valorDeCompra

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Ano lancamento: {self.anoLancamento}")
        print(f"Valor de compra: R$ {self.valorDeCompra}")