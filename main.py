from Objetos.Documentario import *
from Objetos.Filme import *
from Objetos.Serie import *
from Objetos.PlayList import *

documentario = Documentario(5,"Alieniginas do pasado", 2010, 555.55)
filme = Filme("Vingadores",2011, True, 1255.55)
serie = Serie("TWD", 8, 2007, 88)

listaProgramasTv = [documentario, filme, serie]

playList_Ferias = PlayList("Ferias", listaProgramasTv)

print(len(playList_Ferias))

# for programaTv in playList_Ferias:
    # programaTv.exibirDados()

# documentario.exibirDados()
# filme.exibirDados()
# filme.vender(2000)
