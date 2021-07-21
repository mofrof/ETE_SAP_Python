from types import MethodType
from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import redirect
from Objetos.Filme import *

webApp = Flask(__name__)

filme1 = Filme('Matrix', 1999, True, 50.55)
filme2 = Filme('Street of fear', 2021, True, 150.55)
filme3 = Filme('Avengers: End game', 2019, True, 255.55)

filmes = [filme1, filme2, filme3]


@webApp.route('/')
def inicio():
    return render_template('index.html', titulo='Menu principal')


@webApp.route('/filmes')
def listaFilmes():
    return render_template('listar_filmes.html', titulo="Lista de filmes", listaFilmes=filmes)


@webApp.route('/filme/novo')
def novoFilme():
    return render_template('cadastrar_filme.html', titulo="Cadastrar novo filme")


@webApp.route('/filme/cadastrar', methods=['POST', ])
def cadastrarFilme():
    filme4 = Filme(request.form.get('nome', type=int), request.form.get('anoLancamento', type=int),
                   request.form.get('disponivel', type=bool), request.form.get('valorCompra', type=float))

    filmes.append(filme4)
    return redirect('/filmes')


@webApp.route('/filme/excluir')
def excluirFilme():
    index = request.args.get('index', type=int)
    filmes.pop(index)
    return redirect('/filmes')


@webApp.route('/filme/alterar')
def alterarFilme():
    index = request.args.get('index', type=int)
    return render_template('alterar_filme.html', titulo="Alterar filme", filme=filmes[index], index=index)


@webApp.route('/filme/update', methods=['POST', ])
def updateFilme():
    filme = filmes[request.form.get('index', type=int)]
    filme.nome = request.form.get('nome', type=str)
    filme.anoLancamento = request.form.get('anoLancamento', type=int)
    filme.valorDeCompra = request.form.get('valorCompra', type=float)
    filme.disponivel = request.form.get('disponivel', type=bool)

    return redirect('/filmes')


webApp.run(debug="enable")
