class Venda():
    def __init__(self, nomeVendedor, produto):
        self.__nomeVendedor = nomeVendedor
        self.__produto = produto

    # GET
    @property
    def produto(self):
        return self.__produto

    # SET
    @produto.setter
    def produto(self, novoProduto):
        if(novoProduto != None):
            self.__produto = novoProduto

    def descontoEspecial(self,porcentagemDesconto):
        return self.__produto.pegarValorTotal() - (self.__produto.pegarValorTotal() * porcentagemDesconto)