#Classes
class IST:
    def __init__(self, nome, altura, idade):              #__init__ - Inicializador da classe, fodasse o self mas tem que ser escrito
        self.__nome = nome
        self.__altura = altura                            #self - basicamene diz tu propria tens uma altura e tu propria tens uma idade para guardar os dados em algum lado
        self.__idade = idade
    def set_altura(self, altura):
        self.__altura = altura
    def __str__(self) -> str:               #__str__ passa algo para uma string
        return f"Esta pessoa do IST chama-se {self.__nome}"
    def __repr__(self) -> str:
        return f"Esta pessoa do IST chama-se {self.__nome}"
    def get_altura(self):
        return self.__altura


class Aluno(IST):
    def __init__(self, nome, altura, idade, curso):
        super().__init__(nome, altura, idade)      #super.init faz com que a class aluno comece exatamente da mesma maneira que a classe ist e só depois adicione as outras variaveis neste caso o curso
        self.__curso = curso                    #se tivesse os parametros privados nem a classe aluno conseguiria aceder à altura do Vasco
    def get_curso(self):
        return self.__curso
    def get_altura(self) -> float:
        return self.__altura


Vasco = Aluno("Vasco", 180, 19, "LEFT")     #Se tiver só um tracinho seria um dado protegido
                                            #Diferença entre protegido e privado : parametro privado nao consegue ser acedido por classes hereditarias só consegue ser acedido pela propria classe e o protegido pode ser acedido por classes hereditarias
Freitas = IST("Freitas", 165, 59)


print(Vasco.get_altura())
#O python sabe que tem de ir buscar o segundo get_altura porque o tipo de objeto Vasco é do tipo aluno
#Se quisesse chamar o primeiro get_altura teria de colocar um objeto do tipo IST
#Ex: O Vasco é do tipo Aluno e o Freitas é do tipo IST

print(str(Vasco))
print(repr(Vasco))



#Se para ordenar uma lista usassemos o metodo de ver o menor numero e colocar no primerio lugar da lista teria que percorrer a lista n vezes por cada elemento por isso O(n)=n**2
#Tenho uma lista vejo os dois primeiros elementos e depois O(n)=n**2

#Merge sort (O(n)=nlog(n))


#Se tivermos n livros de peso x : valor x ->ratio peso valor

# 1:1 -> 1 
# 3:4 -> 1.33
# 4:5 -> 1.25
# 5:7 -> 1.4
# ...

#Qual o método mais eficiente de conseguir meter os livros numa mochila que só aguente peso 7 e que tenha o maior valor possível
#Dica: com matrizes dá para resolver este problema, logo desiste.