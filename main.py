from flask.helpers import url_for
from Objetos.Filme import Filme
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

webApp = Flask(__name__)

matrix = Filme("Matrix", 1998, True, 150.50)
vingadores = Filme("Vingadores", 2019, True, 250)
ghost = Filme("Ghost", 1986, False, 355.75)

filmes = [matrix, vingadores, ghost]


@webApp.route('/filmes')
def readFilmes():
    return render_template('lista_filmes.html', listaFimes=filmes)


@webApp.route('/filme/cadastro')
def cadastroFilme():
    return render_template('cadastro_filmes.html')


@webApp.route('/filme/cadastrar')
def createFilme():
    nome = request.args.get('nome')
    anoLancamento = request.args.get('anoLancamento')
    valorDeCompra = request.args.get('valorDeCompra')
    if(request.args.get('disponivel') == 'on'):
        disponivel = True
    else:
        disponivel = False

    novoFilme = Filme(nome, anoLancamento, disponivel, valorDeCompra)

    filmes.append(novoFilme)

    return redirect('/filmes')


@webApp.route('/filme/excluir')
def deleteFilme():
    index = int(request.args.get("index"))
    filmes.pop(index)
    return redirect("/filmes")

@webApp.route('/filme/alterar')
def alterarFilme():
    index = int(request.args.get("index"))
    filme = filmes[index]
    return render_template("alterar_filmes.html", filme = filme, index = index)

@webApp.route('/filme/update')
def updateFilme():
    index = int(request.args.get("index"))
    filme = filmes[index]
    filme.nome = request.args.get('nome')
    filme.anoLancamento = request.args.get('anoLancamento')
    filme.valorDeCompra = request.args.get('valorDeCompra')
    if(request.args.get('disponivel') == 'on'):
        filme.disponivel = True
    else:
        filme.disponivel = False
    
    return redirect('/filmes')
    





@webApp.route('/')
def index():
    return render_template('index.html')


webApp.run(debug="enable")
