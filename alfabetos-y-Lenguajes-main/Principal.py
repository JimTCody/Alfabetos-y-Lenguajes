import sys
import random
from PyQt5.QtCore import QPropertyAnimation
from clases.Alfabeto import Alfabeto
from clases.Lenguaje import Lenguaje
from disenio.interfaz import *

class Principal(QtWidgets.QWidget):


    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)

        self.ui.btnMenu.clicked.connect(self.transicionLateral)
        self.ui.btnUnion.clicked.connect(self.mostrarDatos)
        self.ui.btninterseccion.clicked.connect(self.resinterseccion)
        self.ui.btnDiferencia.clicked.connect(self.resdiferencia)
        self.ui.cerraduraEstrella.clicked.connect(self.cerraduraEstrella)
        self.ui.crearLenguajes.clicked.connect(self.llenarLenguajes)
        self.ui.crearLenguajes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paginaLenguajes))
        self.ui.btnAlfabetos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.paginaAlfabetos))
        self.ui.btnLenUnion.clicked.connect(self.lenUnion)
        self.ui.btnLenDiferencia.clicked.connect(self.lenDiferencia)
        self.ui.btnLenInterseccion.clicked.connect(self.lenInterseccion)
        self.ui.btnLenConcatenacion.clicked.connect(self.lenConcatenacion)
        self.ui.btnLenPotencia.clicked.connect(self.lenPotencia)
        self.ui.btnLenInvertir.clicked.connect(self.lenInvertir)
        self.ui.btnLenCardinalidad.clicked.connect(self.lenCardinalidad)



    def transicionLateral(self):
        if True:
            width = self.ui.frameLateral.width()
            normal = 0

        if width == 0:
            extender = 250
        else:
            extender = normal
        self.animacion = QPropertyAnimation(self.ui.frameLateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

    def mostrarDatos(self):
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.union(alfabeto2.getConjunto())))
        if self.ui.plainTextResultados.toPlainText()=='{}':
            self.ui.plainTextResultados.setPlainText("Los alfabetos se encuentran vacíos")

    def resinterseccion(self):
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.intersección(alfabeto2.getConjunto())))
        if self.ui.plainTextResultados.toPlainText()=='{}':
            self.ui.plainTextResultados.setPlainText("Los alfabetos se encuentran vacíos")

    def resdiferencia(self):
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        self.ui.plainTextResultados.setPlainText(str(alfabeto1.diferencia(alfabeto2.getConjunto())))
        if self.ui.plainTextResultados.toPlainText()=='{}':
            self.ui.plainTextResultados.setPlainText("Los alfabetos se encuentran vacíos")



    def lenUnion(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        self.ui.plainTextResultados2.setPlainText(str(lenguaje1) + "\n" +
                                                   str(lenguaje2) + "\n" +
                                                   str(lenguaje1.union(lenguaje2.getConjunto())))

    def lenDiferencia(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        self.ui.plainTextResultados2.setPlainText(str(lenguaje1) + "\n" +
                                                 str(lenguaje2) + "\n" +
                                                 str(lenguaje1.diferencia(lenguaje2.getConjunto())))

    def lenInterseccion(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        self.ui.plainTextResultados2.setPlainText(str(lenguaje1) + "\n" +
                                                 str(lenguaje2) + "\n" +
                                                 str(lenguaje1.intersección(lenguaje2.getConjunto())))

    def lenConcatenacion(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        ListaConcat = ['⌀']
        for i in list(lenguaje1.getConjunto()):
            palabra1 = (i)
            for i in list(lenguaje2.getConjunto()):
                palabraConcat = palabra1 + (i)
                ListaConcat.append(palabraConcat)
        self.ui.plainTextResultados2.setPlainText(str(lenguaje1.getConjunto()) + "\n" +
                                                 str(lenguaje2.getConjunto()) + "\n" +
                                                 "La concatenación es:" + str(list(ListaConcat)))

    def lenPotencia(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        ListaPow = [""]
        ListaPow2 = [""]
        potencia=self.ui.selecPotencia_2.value()

        if potencia != 0:
            for i in range(potencia):
                for i in list(ListaPow):
                    palabra1 = (i)
                    for i in list(lenguaje1.getConjunto()):
                        palabraConcat = palabra1 + (i)
                        ListaPow.append(palabraConcat)
        ListaPow[:0]='⌀'
        ListaPow=list(set(ListaPow))
        ListaPow.sort(key=len)
        del ListaPow[0]

        if potencia != 0:
            for j in range(potencia):
                for j in list(ListaPow2):
                    palabra2 = (j)
                    for j in list(lenguaje2.getConjunto()):
                        palabraConcat2 = palabra2 + (j)
                        ListaPow2.append(palabraConcat2)

        ListaPow2=list(set(ListaPow2))
        ListaPow2.sort(key=len)
        del ListaPow2[0]
        ListaPow2[:0] = '⌀'

        self.ui.plainTextResultados2.setPlainText(str(lenguaje1.getConjunto()) + "\n" +
                                                 "La Potencia del lenguaje 1 es:" + str(ListaPow)
                                                  + "\n" +
                                                  "La Potencia del lenguaje 2 es:" + str(ListaPow2))

    def lenInvertir(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        ListaINV = []
        ListaINV2 = []

        for i in list(lenguaje1.getConjunto()):
            palabraINV = ((i)[::-1])
            ListaINV.append(palabraINV)

        for i in list(lenguaje2.getConjunto()):
            palabraINV2 = ((i)[::-1])
            ListaINV2.append(palabraINV2)

        self.ui.plainTextResultados2.setPlainText("Lenguaje1:" + str(lenguaje1.getConjunto())
                                                  + "\n" + str(list(ListaINV)) + "\n" +
                                                  "Lenguaje2:" + str(lenguaje2.getConjunto())
                                                  + "\n" + str(list(ListaINV2)))

    def lenCardinalidad(self):
        lenguaje1 = Lenguaje(self.ui.mostrarLenguaje1.text().split())
        lenguaje2 = Lenguaje(self.ui.mostrarLenguaje2.text().split())

        self.ui.plainTextResultados2.setPlainText("La cardinalidad del lenguaje 1 es:" + str(len(set(lenguaje1.getConjunto())))
                                                  + "\n" +
                                                  "La cardinalidad del lenguaje 2 es:" + str(len(set(lenguaje2.getConjunto()))))

    def cerraduraEstrella(self):
        cerradura1 = []
        cerradura2 = []
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        alfabeto2 = Alfabeto(self.ui.lineEditConjuntoB.text().split())
        power = self.ui.selecPotencia_1.value()
        while len(set(cerradura1)) != power:
            potencia = random.randint(1, 5)
            palabra = ""
            for i in range(potencia):
                letra = random.choice(list(alfabeto1.getConjunto()))
                palabra = letra + palabra
            cerradura1.append(palabra)

        while len(set(cerradura2)) != power:
            potencia = random.randint(1, 5)
            palabra = ""
            for i in range(potencia):
                letra = random.choice(list(alfabeto2.getConjunto()))
                palabra = letra + palabra
            cerradura2.append(palabra)

        self.ui.plainTextResultados.setPlainText("La cerradura de estrella del primer alfabeto es: \n"+
                                                 str(set(cerradura1)) +"\n\n"+
                                                 "La cerradura de estrella del segundo alfabeto es: \n"+
                                                 str(set(cerradura2)))
        check=str(set(cerradura2))
        if check=='set()':
            self.ui.plainTextResultados.setPlainText("Los alfabetos se encuentran vacíos")



    def llenarLenguajes(self):
        lenguaje1 = Lenguaje(self.crearLenguajes())
        lenguaje2 = Lenguaje(self.crearLenguajes())

        lenguaje1=str(lenguaje1).strip("{}")
        lenguaje1=lenguaje1.replace(","," ")
        self.ui.mostrarLenguaje1.setText(lenguaje1)

        lenguaje2 = str(lenguaje2).strip("{}")
        lenguaje2 = lenguaje2.replace(",", " ")
        self.ui.mostrarLenguaje2.setText(lenguaje2)

    def crearLenguajes(self):
        if self.ui.lineEditConjuntoA.text()=='':
            self.ui.plainTextResultados.setPlainText("El alfabeto A se encuentra vacío")
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.paginaLenguajes)
        lenguaje = []
        alfabeto1 = Alfabeto(self.ui.lineEditConjuntoA.text().split())
        power=self.ui.selecPotencia_1.value()
        while len(set(lenguaje))!= power:
            potencia = random.randint(1, power)
            palabra = ""
            for i in range(potencia):
                letra = random.choice(list(alfabeto1.getConjunto()))
                palabra = letra + palabra
            lenguaje.append(palabra)
        return set(lenguaje)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Principal()
    GUI.show()
    sys.exit(app.exec_())
