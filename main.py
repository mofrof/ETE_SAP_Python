from types import MethodType
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from werkzeug.utils import redirect
from Objetos.Filme import *
import json

webApp = Flask(__name__)


filme1 = Filme('Matrix', 1999, True, 50.55)
filme2 = Filme('Street of fear', 2021, True, 150.55)
filme3 = Filme('Avengers: End game', 2019, True, 255.55)

filmes = [filme1, filme2, filme3]


@webApp.route('/')
def inicio():
    return render_template('index.html', titulo='RESUMO', disponiveis=3, indisponiveis=0)


@webApp.route('/filmes')
def listaFilmes():
    return render_template('listar_filmes.html', titulo="Lista de filmes", listaFilmes=filmes)


@webApp.route('/filme/novo')
def novoFilme():
    return render_template('cadastrar_filme.html', titulo="Cadastrar novo filme")


@webApp.route('/filme/cadastrar', methods=['POST', ])
def cadastrarFilme():
    nome = request.form.get('nome', type=str)
    anoLancamento = request.form.get('anoLancamento', type=int)
    valorDeCompra = request.form.get('valorCompra', type=float)
    disponivel = False
    if(request.form.get('disponivel', type=bool) ):
        disponivel = True
    filme = Filme(nome,anoLancamento,disponivel,valorDeCompra)
    filmes.append(filme)

    return redirect('/filmes')

@webApp.route('/filme/excluir/<int:index>')
def excluirFilme(index):
    filmes.pop(index)
    return redirect('/filmes')


@webApp.route('/filme/alterar/<int:index>')
def alterarFilme(index):
    return render_template('alterar_filme.html', titulo="Alterar filme", filme=filmes[index], index=index)

@webApp.route('/filme/update', methods=['POST', ])
def updateFilme():
    filme = filmes[request.form.get('index', type=int)]
    filme.nome = request.form.get('nome', type=str)
    filme.anoLancamento = request.form.get('anoLancamento', type=int)
    filme.valorDeCompra = request.form.get('valorCompra', type=float)
    filme.disponivel = False
    if(request.form.get('disponivel', type=bool) ):
        filme.disponivel = True
    
    return redirect('/filmes')

@webApp.route('/login')
def logar():
    return render_template('login.html')

@webApp.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session ['usuario_logado'] = request.form['usuario']
        return redirect('/')
    else :
        return redirect ('/login')



webApp.run(debug="enable")
