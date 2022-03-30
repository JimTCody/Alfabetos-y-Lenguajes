from clases.Alfabeto import Alfabeto
from itertools import  product
import string, random

class Lenguaje(Alfabeto):
    def concatenacion(self, lenguajeB):
        concatenado = list(product(self.conjunto, lenguajeB))
        return set(concatenado)

    pass

 #
 #    alfabeto2STR = input('Digite el alfabeto separado por espacios: ')
 #    alfabeto2LIST = alfabeto2STR.split(' ')
 #    print(alfabeto2LIST)
 #    import string, random
 #
 #    alfabeto1STR = input('Digite el alfabeto separado por espacios: ')
 #    alfabeto1LIST = alfabeto1STR.split(' ')
 #    print(alfabeto1LIST)
 #
 #    def union(alfabeto1LIST, alfabeto2LIST):
 #        alfabeto3 = list(set().union(alfabeto1LIST, alfabeto2LIST))
 #        return alfabeto3
 #
 #    print(union(alfabeto1LIST, alfabeto2LIST))
 #
 #    cantidad = (int(input("Digite la cantidad de palabras que desea generar: ")))
 #    lenguaje1 = []
 #    for i in range(cantidad):
 #
 #        potencia = random.randint(1, 10)
 #        palabra = ""
 #        for i in range(potencia):
 #            letra = random.choice(union(alfabeto1LIST, alfabeto2LIST))
 #            palabra = str(letra) + str(palabra)
 #        lenguaje1.append(palabra)
 #    print(lenguaje1)



