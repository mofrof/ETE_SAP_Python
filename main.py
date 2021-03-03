listaDeFilmes = []
listaDeSeries = []

def init():
    def exibirContagemFilmesESeries(opcaoFilmeOuSerie):
            if opcaoFilmeOuSerie == 1:
                print(len(listaDeFilmes))
            elif opcaoFilmeOuSerie == 2:
                print(len(listaDeSeries))
            else:
                print("Erro interno, falar com desenvolvedor")

            print("Contagem geral:")
            print("Filmes:")
            print(len(listaDeFilmes))
            print("Series:")
            print(len(listaDeSeries))
            print(len(listaDeFilmes) + len(listaDeSeries))
    def menuAdicionar():
        repetirMenuPrincipal = True
        while repetirMenuPrincipal:
            print("================Adicionar===================")
            print("1 - Adicionar Filme")
            print("2 - Adicionar Serie")
            print("3 - sair")
            opcaoDoUsuario = int(input("Digite sua opção: "))
            if opcaoDoUsuario == 1:
                listaDeFilmes.append(input("Digite o nome do Filme: "))
            elif opcaoDoUsuario == 2:
                listaDeSeries.append(input("Digite o nome do Serie: "))
            elif opcaoDoUsuario == 3:
                repetirMenuPrincipal = False
            else:
                print("Opção invalida !!!")

            print("Item Adicionado com sucesso")

    def exibirListaGeral():
        print(listaDeFilmes + listaDeSeries)
    def menuExibirListas():
        repetirMenuPrincipal = True
        while repetirMenuPrincipal:
            print("================Dados dos sistema===================")
            print("1 - Lista Gereal")
            print("2 - Contagem Series")
            print("3 - Contagem Filmes")
            print("4 - sair")
            opcaoDoUsuario = int(input("Digite sua opção: "))
            if opcaoDoUsuario == 1 :
                exibirListaGeral()
            elif opcaoDoUsuario == 2 :
                exibirContagemFilmesESeries(2)
            elif opcaoDoUsuario == 3 :
                exibirContagemFilmesESeries(1)
            else:
                repetirMenuPrincipal = False

    repetirMenuPrincipal = True
    while repetirMenuPrincipal:
        print("================Listas de Filmes e Series===================")
        print("1 - adicionar nova serie a lista")
        print("2 - Ver lista geral")
        print("3 - sair")

        opcaoDoUsuario = int(input("Digite sua opção: "))
        if opcaoDoUsuario == 1 :
            menuAdicionar()
        elif opcaoDoUsuario == 2 :
            menuExibirListas()
        elif opcaoDoUsuario == 3 :
            repetirMenuPrincipal = False
        else:
            print("Erro opção invalida !!!")

init()