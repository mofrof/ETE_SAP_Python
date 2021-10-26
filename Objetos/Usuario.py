class Usuario:
    def __init__(self, login, senha, nivel) -> None:
        self.login = login
        self.senha = senha
        self.nivel = nivel
    
    def senhaHeValida(self, senhaComparacao) -> bool:
        return self.senha == senhaComparacao 

    def verificarNivelAcesso():
        pass