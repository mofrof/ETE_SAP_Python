from Objetos.Filme import Filme
from flask import Flask
from flask import render_template

webApp = Flask(__name__)

matrix = Filme("Matrix", 1998, True, 150.50)
vingadores = Filme("Vingadores", 2019, True, 250)
ghost = Filme("Ghost", 1986, False, 355.75)

filmes = [matrix, vingadores, ghost]

@webApp.route('/filmes')
def readFilmes():
    return render_template('lista_filmes.html',listaFimes = filmes)

@webApp.route('/')
def index():
    return render_template('index.html')

webApp.run(debug="enable")