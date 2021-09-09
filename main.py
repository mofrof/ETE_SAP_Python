# from flask.helpers import url_for
from Objetos.Filme import Filme
from flask import Flask, render_template, request, redirect

webApp = Flask(__name__)

matrix = Filme("Matrix", 1998, True, 150.50)
vingadores = Filme("Vingadores", 2019, True, 250)
ghost = Filme("Ghost", 1986, False, 355.75)

listaFilmes = [matrix, vingadores, ghost]

def pegarQuantidadeFilmesDisponiveis(listaFilmes):
    quant = 0
    for filme in listaFilmes:
        if filme.disponivel:
            quant = quant + 1
    return quant

def pegarQuantidadeFilmesIndisponiveis(listaFilmes):
    quant = 0
    for filme in listaFilmes:
        if not filme.disponivel:
            quant = quant + 1
    return quant

@webApp.route('/filmes')
def mostrarFilmes():
    return render_template('lista_filmes.html', listaFilmes= listaFilmes)


@webApp.route('/filme/cadastro')
def exibirTelaDeCadastroFilme():
    return render_template('cadastro_filmes.html')


@webApp.route('/filme/cadastrar',methods=['POST',])
def cadastrarFilme():
    nome = request.form["nome"]
    anoLancamento = request.form["anoLancamento"] 
    valorDeCompra = request.form["valorDeCompra"]
    if "disponivel" in request.form:
        disponivel = True
    else:
        disponivel = False

    novoFilme = Filme(nome, anoLancamento, disponivel, valorDeCompra)

    listaFilmes.append(novoFilme)

    return redirect('/filmes')


@webApp.route('/filme/excluir/<int:index>')
def excluirFilme(index):
    listaFilmes.pop(index)
    return redirect("/filmes")

@webApp.route('/filme/altera/<int:index>')
def exibirTelaAlterarFilme(index):
    filme = listaFilmes[index]
    return render_template("alterar_filmes.html", filme = filme, index = index)

@webApp.route('/filme/alterar', methods=['POST',])
def alterarFilme():
    index = int(request.form["index"]) 
    filme = listaFilmes[index]
    filme.nome = request.form["nome"]
    filme.anoLancamento = request.form["anoLancamento"]
    filme.valorDeCompra = request.form["valorDeCompra"]
    if "disponivel" in request.form:
        filme.disponivel = True
    else:
        filme.disponivel = False
    
    return redirect('/filmes')
    
@webApp.route('/')
def telaPrincipal():
    quantDisp = pegarQuantidadeFilmesDisponiveis(listaFilmes)
    quantIndisp = pegarQuantidadeFilmesIndisponiveis(listaFilmes)
    return render_template('index.html', quantDisp = quantDisp, quantIndisp = quantIndisp)

@webApp.route('/login')
def exebirPaginaAcesso():
    return render_template('login.html')

webApp.run(debug="enable")
