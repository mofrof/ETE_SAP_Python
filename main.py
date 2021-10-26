from flask.helpers import url_for
from Objetos.Filme import Filme
from Objetos.Usuario import Usuario
from flask import Flask, render_template, request, redirect
from flask import session
from flask import flash

webApp = Flask(__name__)
webApp.secret_key = 'ETE'

admin = Usuario("Admin", "Admin", "adm")
zezinho = Usuario("Ze", "sorvete", "comum")

matrix = Filme("Matrix", 1998, True, 150.50)
vingadores = Filme("Vingadores", 2019, True, 250)
ghost = Filme("Ghost", 1986, False, 355.75)

listaFilmes = [matrix, vingadores, ghost]
listaUsuarios = [admin, zezinho]

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

def usuarioLogado()->bool:
    if session["usuario_logado"] == None or 'usuario_logado' not in session:
        return False
    return True

def usuarioExiste(login)->bool:
    for usuario in listaUsuarios:
        if usuario.login == login:
            return True
    
    return False

def pegarUsuario(login)->Usuario:
    for usuario in listaUsuarios:
        if usuario.login == login:
            return usuario
    return None

@webApp.route('/filmes')
def mostrarFilmes():
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('mostrarFilmes')))
    return render_template('lista_filmes.html', listaFilmes= listaFilmes)


@webApp.route('/filme/cadastro')
def exibirTelaDeCadastroFilme():
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('exibirTelaDeCadastroFilme')))
    return render_template('cadastro_filmes.html')

@webApp.route('/filme/cadastrar',methods=['POST',])
def cadastrarFilme():
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('telaPrincipal')))

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
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('telaPrincipal')))

    listaFilmes.pop(index)
    return redirect("/filmes")

@webApp.route('/filme/altera/<int:index>')
def exibirTelaAlterarFilme(index):
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('telaPrincipal')))

    filme = listaFilmes[index]
    return render_template("alterar_filmes.html", filme = filme, index = index)

@webApp.route('/filme/alterar', methods=['POST',])
def alterarFilme():
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('telaPrincipal')))

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
    if not usuarioLogado():
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = url_for('telaPrincipal')))
    quantDisp = pegarQuantidadeFilmesDisponiveis(listaFilmes)
    quantIndisp = pegarQuantidadeFilmesIndisponiveis(listaFilmes)
    return render_template('index.html', quantDisp = quantDisp, quantIndisp = quantIndisp)

@webApp.route('/login')
def exebirPaginaAcesso():
    proximaPagina = request.args.get('proximaPagina')
    return render_template('login.html', proximaPagina = proximaPagina)

@webApp.route('/autenticar', methods=['POST',])
def autenticarUsuario():
    login = request.form["login"]
    senha = request.form["senha"]
    proximaPagina = request.form["proximaPagina"]
    
    if not usuarioExiste(login):
        flash(f"Login {login} nao existe!")
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = proximaPagina))
    
    usuario = pegarUsuario(login)

    if not usuario.senhaHeValida(senha):
        flash(f"Senha incorreta!")
        return redirect(url_for('exebirPaginaAcesso', proximaPagina = proximaPagina))
    
    flash(f"Bem vindo {usuario.login} !")
    session['usuario_logado'] = usuario.login
    session['nivel'] = usuario.nivel
    
    return redirect(proximaPagina)

@webApp.route('/logout')
def lgout():
    session['usuario_logado'] = None
    return redirect('/login')

webApp.run(debug="enable")
