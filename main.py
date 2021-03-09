listaDeFilmes = []
listaDeSeries = []

def init():
    def contadorDeListas(indicacaoDeLista):
            if indicacaoDeLista == 1:
                print("Total de Filmes:")
                print(len(listaDeFilmes))
            elif indicacaoDeLista == 2:
                print("Total de Series:")
                print(len(listaDeSeries))
            else:
                print(len(listaDeFilmes)+len(listaDeSeries))

    def menuAdicionar():
        repetirMenuAdicionar = True

        while repetirMenuAdicionar:
            print("================Adicionar===================")
            print("1 - Adicionar Filme")
            print("2 - Adicionar Serie")
            print("3 - sair")

            opcaoDoUsuarioNoMenuAdicionar = int(input("Digite sua opção: "))

            if opcaoDoUsuarioNoMenuAdicionar == 1:
                listaDeFilmes.append(input("Digite o nome do Filme: "))
                print("Item Adicionado com sucesso")

            elif opcaoDoUsuarioNoMenuAdicionar == 2:
                listaDeSeries.append(input("Digite o nome do Serie: "))
                print("Item Adicionado com sucesso")

            elif opcaoDoUsuarioNoMenuAdicionar == 3:
                repetirMenuAdicionar = False

            else:
                print("Opção invalida !!!")

    def exebiListaGeral():
        print(listaDeFilmes + listaDeSeries)

    def menuLista():
        repetirMenuLista = True
        while repetirMenuLista:
            print("================Dados dos sistema===================")
            print("1 - Lista Gereal")
            print("2 - Contagem Series")
            print("3 - Contagem Filmes")
            print("4 - Sair")
            opcaoDoUsuarioNoMenuLista = int(input("Digite sua opção: "))
            if opcaoDoUsuarioNoMenuLista == 1 :
                exebiListaGeral()
            elif opcaoDoUsuarioNoMenuLista == 2 :
                contadorDeListas(2)
            elif opcaoDoUsuarioNoMenuLista == 3 :
                contadorDeListas(1)
            else:
                repetirMenuLista = False

    repetirMenuPrincipal = True
    while repetirMenuPrincipal:
        print("================Listas de Filmes e Series===================")
        print("1 - Adicionar nova filme ou serie a lista")
        print("2 - Ver lista geral")
        print("3 - sair")
        opcaoDoUsuarioNoMenuPrincpal = int(input("Digite sua opção: "))
        if opcaoDoUsuarioNoMenuPrincpal == 1 :
            menuAdicionar()
        elif opcaoDoUsuarioNoMenuPrincpal == 2 :
            menuLista()
        elif opcaoDoUsuarioNoMenuPrincpal == 3:
             repetirMenuPrincipal = False
        else:
            print("Opção é invalida!!")

init()