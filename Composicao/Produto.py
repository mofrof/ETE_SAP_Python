class Produto():
    def __init__(self, nome, valor, quantidade):
        self.nome = nome
        self.__valor = valor
        self.__quantidade = quantidade

    def pegarValorTotal(self):
        return self.__quantidade * self.__valor
