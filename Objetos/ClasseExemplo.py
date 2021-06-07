#Como classe sou o Mode|Forma|Estrutura
#que define o objeto
class ClasseExemplo:

    def __init__(self, atributo1, atributo2, atributoPublico):
        print("sou o metodo construtor")
        self.atributoPublico = atributoPublico
        #Somos atributos privados
        self.__atributo1 = atributo1
        self.__atributo2 = atributo2

    def subtrairValorDoAtributo1(self, valor):
        print("Sou um metodo publico")
        return self.__atributo1 - valor

    def somarAtributos(self):
        print("Sou um metodo publico")
        if self.__atributo1ValidoParaCalculo():
            return self.__atributo1 + self.__atributo2 + self.atributoPublico
        
        return self.__atributo2

    def __atributo1ValidoParaCalculo(self):
        print("Sou um metodo privado")
        return self.__atributo1 >= 10

    @property
    def atributo1(self):
        print("Sou um metodo Get")
        return self.__atributo1
    
    @atributo1.setter
    def atributo1(self, novoValor):
        print("Sou um metodo Set")
        self.__atributo1 = novoValor

    @staticmethod
    def metodoDaClasse():
        return "Eu pertenço a classe e não ao objeto"
    
#Objeto construido apartir da classeExemplo
objetoDaClasseExemplo = ClasseExemplo(10,20,30)

#outro Objeto tambem construido apartir da classeExemplo
outroObjetoDaClasseExemplo = ClasseExemplo(30,10,50)

#utilizando metodos do objeto
objetoDaClasseExemplo.subtrairValorDoAtributo1(5)

objetoDaClasseExemplo.somarAtributos()

#utilizando metodos Get
print(outroObjetoDaClasseExemplo.atributo1)

#utilizando metodos SET
outroObjetoDaClasseExemplo.atributo1 = 90

#utilizando metodo estatico
#não precisa criar um objeto para utilizar esse metodo
ClasseExemplo.metodoDaClasse()