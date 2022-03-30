import random
from clases.Alfabeto import *
from Principal import *
from clases.Lenguaje import Lenguaje

ListaA = ['a']
ListaB = ['b']
ListaC=ListaB
ListaPow= ['⌀']
potencia=30
for i in ListaA:
    for j in ListaA:
        j = j+i
        for k in ListaA:
            k = k+j
            for l in ListaA:
                l = l + k
                for m in ListaA:
                    m = m + l
                    ListaPow.append(m)
                ListaPow.append(l)
            ListaPow.append(k)
        ListaPow.append(j)
    ListaPow.append(i)
ListaPow.sort(key=len)
print(ListaPow)
print(ListaPow[0:potencia])
ListaA = ['a']