a = []
d = []

def init():
    def j(k):
            if k == 1:
                print(len(a))
            else:
                print(d.count)
            
            print(len(a)+len(d))
    def i():
        f = True
        while f:
            print("================Adicionar===================")
            print("1 - Adicionar Filme")
            print("2 - Adicionar Serie")
            print("3 - sair")
            e = int(input("Digite sua opção: "))
            if e == 1:
                a.append(input("Digite o nome do Filme: "))
            elif e == 2:
                d.append(input("Digite o nome do Serie: "))
            else:
                f = False
            print("Item Adicionado com sucesso")

    def g():
        print(a + d)
    def k():
        l = True
        while l:
            print("================Dados dos sistema===================")
            print("1 - Lista Gereal")
            print("2 - contagem Series")
            print("3 - contagem Filmes")
            print("4 - sair")
            m = int(input("Digite sua opção: "))
            if m == 1 :
                g()
            elif m == 2 :
                j(2)
            elif m == 3 :
                j(1)
            else:
                b = False

    saidaDoMenuPrincipal = True
    while saidaDoMenuPrincipal:
        print("================Listas de Filmes e Series===================")
        print("1 - adicionar nova serie a lista")
        print("2 - Ver lista geral")
        print("3 - sair")
        opcaoDoUsuario = int(input("Digite sua opção: "))
        if opcaoDoUsuario == 1 :
            i()
        elif opcaoDoUsuario == 2 :
            k()
        else:
            saidaDoMenuPrincipal = False

init()