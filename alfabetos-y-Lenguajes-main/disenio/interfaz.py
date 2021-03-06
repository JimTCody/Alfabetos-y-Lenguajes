# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(821, 498)
        ventanaPrincipal.setMaximumSize(QtCore.QSize(821, 498))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../iconos/languages.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventanaPrincipal.setWindowIcon(icon)
        ventanaPrincipal.setStyleSheet("border:0px\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(ventanaPrincipal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Superior = QtWidgets.QFrame(ventanaPrincipal)
        self.Superior.setMinimumSize(QtCore.QSize(0, 40))
        self.Superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Superior.setStyleSheet("QFrame,QPushButton{\n"
"background-color:Black;\n"
"}\n"
"QPushButton{\n"
" border:2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color:rgb(245, 121, 0);\n"
"}")
        self.Superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Superior.setObjectName("Superior")
        self.btnMenu = QtWidgets.QPushButton(self.Superior)
        self.btnMenu.setGeometry(QtCore.QRect(0, -6, 250, 51))
        self.btnMenu.setMaximumSize(QtCore.QSize(260, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.btnMenu.setPalette(palette)
        self.btnMenu.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnMenu.setAutoFillBackground(False)
        self.btnMenu.setStyleSheet("QPushButtom{\n"
"color:white;\n"
"border-bottom:1px solid white;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../iconos/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon1)
        self.btnMenu.setIconSize(QtCore.QSize(40, 40))
        self.btnMenu.setObjectName("btnMenu")
        self.verticalLayout.addWidget(self.Superior)
        self.inferior = QtWidgets.QFrame(ventanaPrincipal)
        self.inferior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.inferior.setFrameShadow(QtWidgets.QFrame.Plain)
        self.inferior.setLineWidth(0)
        self.inferior.setObjectName("inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameLateral = QtWidgets.QFrame(self.inferior)
        self.frameLateral.setMinimumSize(QtCore.QSize(0, 0))
        self.frameLateral.setMaximumSize(QtCore.QSize(0, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frameLateral.setPalette(palette)
        self.frameLateral.setStyleSheet("QFrame{\n"
"background-color:black;\n"
"}\n"
"QPushButton{\n"
"border:1px solid white;\n"
"border-radius:20px;\n"
"color:rgb(255,255,255);\n"
"}\n"
"QFrame:hover{\n"
"border-top:1 px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(245, 121, 0);\n"
"color:rgb(0,0,0);\n"
"}")
        self.frameLateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLateral.setObjectName("frameLateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameLateral)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.btnAlfabetos = QtWidgets.QPushButton(self.frameLateral)
        self.btnAlfabetos.setMinimumSize(QtCore.QSize(0, 40))
        self.btnAlfabetos.setObjectName("btnAlfabetos")
        self.verticalLayout_2.addWidget(self.btnAlfabetos)
        self.btnLenguajes = QtWidgets.QPushButton(self.frameLateral)
        self.btnLenguajes.setMinimumSize(QtCore.QSize(0, 40))
        self.btnLenguajes.setObjectName("btnLenguajes")
        self.verticalLayout_2.addWidget(self.btnLenguajes)
        self.pushButton_4 = QtWidgets.QPushButton(self.frameLateral)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frameLateral)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frameLateral)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton_8 = QtWidgets.QPushButton(self.frameLateral)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgba(191, 64, 64, 0);\n"
"color:white;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../iconos/logo unimag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        spacerItem3 = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frameLateral)
        self.paginas = QtWidgets.QFrame(self.inferior)
        self.paginas.setStyleSheet("")
        self.paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.paginas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.paginas.setLineWidth(0)
        self.paginas.setObjectName("paginas")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.paginas)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.paginas)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 117, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 90, 90, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 159, 159, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 117, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 90, 90, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 159, 159, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 117, 117, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 90, 90, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 42, 42, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 32, 32, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 61, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(191, 64, 64, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet("QWidget{\n"
"background-color:rgb(61,61,61);\n"
"}\n"
"QLineEdit{\n"
"background-color:white;\n"
"}\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.paginaAlfabetos = QtWidgets.QWidget()
        self.paginaAlfabetos.setStyleSheet("QLineEdit{\n"
"border-radius:20px;\n"
"padding-left:20px;\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(245, 121, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border:-1px;\n"
"border:1px solid rgb(245, 121, 0);\n"
"}\n"
"QPlainTextEdit{\n"
"background-color:white;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:30px rgb(245, 121, 0);\n"
"}\n"
"")
        self.paginaAlfabetos.setObjectName("paginaAlfabetos")
        self.lineEditConjuntoA = QtWidgets.QLineEdit(self.paginaAlfabetos)
        self.lineEditConjuntoA.setGeometry(QtCore.QRect(130, 54, 531, 41))
        self.lineEditConjuntoA.setFrame(True)
        self.lineEditConjuntoA.setClearButtonEnabled(True)
        self.lineEditConjuntoA.setObjectName("lineEditConjuntoA")
        self.lineEditConjuntoB = QtWidgets.QLineEdit(self.paginaAlfabetos)
        self.lineEditConjuntoB.setGeometry(QtCore.QRect(130, 110, 531, 41))
        self.lineEditConjuntoB.setClearButtonEnabled(True)
        self.lineEditConjuntoB.setObjectName("lineEditConjuntoB")
        self.btnUnion = QtWidgets.QPushButton(self.paginaAlfabetos)
        self.btnUnion.setGeometry(QtCore.QRect(170, 170, 131, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnUnion.setFont(font)
        self.btnUnion.setObjectName("btnUnion")
        self.btninterseccion = QtWidgets.QPushButton(self.paginaAlfabetos)
        self.btninterseccion.setGeometry(QtCore.QRect(350, 170, 131, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btninterseccion.setFont(font)
        self.btninterseccion.setObjectName("btninterseccion")
        self.btnDiferencia = QtWidgets.QPushButton(self.paginaAlfabetos)
        self.btnDiferencia.setGeometry(QtCore.QRect(510, 170, 131, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnDiferencia.setFont(font)
        self.btnDiferencia.setObjectName("btnDiferencia")
        self.cerraduraEstrella = QtWidgets.QPushButton(self.paginaAlfabetos)
        self.cerraduraEstrella.setGeometry(QtCore.QRect(170, 230, 131, 41))
        self.cerraduraEstrella.setObjectName("cerraduraEstrella")
        self.plainTextResultados = QtWidgets.QPlainTextEdit(self.paginaAlfabetos)
        self.plainTextResultados.setGeometry(QtCore.QRect(60, 290, 691, 141))
        self.plainTextResultados.setObjectName("plainTextResultados")
        self.selecPotencia_1 = QtWidgets.QSpinBox(self.paginaAlfabetos)
        self.selecPotencia_1.setGeometry(QtCore.QRect(360, 230, 101, 41))
        self.selecPotencia_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selecPotencia_1.setObjectName("selecPotencia_1")
        self.crearLenguajes = QtWidgets.QPushButton(self.paginaAlfabetos)
        self.crearLenguajes.setGeometry(QtCore.QRect(510, 230, 131, 41))
        self.crearLenguajes.setObjectName("crearLenguajes")
        self.stackedWidget.addWidget(self.paginaAlfabetos)
        self.paginaLenguajes = QtWidgets.QWidget()
        self.paginaLenguajes.setStyleSheet("QLineEdit{\n"
"border-radius:20px;\n"
"padding-left:20px;\n"
"}\n"
"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(245, 121, 0);\n"
"}\n"
"QLineEdit:hover{\n"
"border:1px solid rgb(245, 121, 0);\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"background-color:white;\n"
"}")
        self.paginaLenguajes.setObjectName("paginaLenguajes")
        self.btnLenUnion = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenUnion.setGeometry(QtCore.QRect(130, 170, 121, 41))
        self.btnLenUnion.setObjectName("btnLenUnion")
        self.plainTextResultados2 = QtWidgets.QPlainTextEdit(self.paginaLenguajes)
        self.plainTextResultados2.setGeometry(QtCore.QRect(110, 270, 571, 171))
        self.plainTextResultados2.setObjectName("plainTextResultados2")
        self.btnLenDiferencia = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenDiferencia.setGeometry(QtCore.QRect(260, 170, 121, 41))
        self.btnLenDiferencia.setObjectName("btnLenDiferencia")
        self.btnLenInterseccion = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenInterseccion.setGeometry(QtCore.QRect(390, 170, 121, 41))
        self.btnLenInterseccion.setObjectName("btnLenInterseccion")
        self.btnLenInvertir = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenInvertir.setGeometry(QtCore.QRect(390, 220, 121, 41))
        self.btnLenInvertir.setObjectName("btnLenInvertir")
        self.btnLenCardinalidad = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenCardinalidad.setGeometry(QtCore.QRect(520, 220, 131, 41))
        self.btnLenCardinalidad.setObjectName("btnLenCardinalidad")
        self.btnLenPotencia = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenPotencia.setGeometry(QtCore.QRect(130, 220, 121, 41))
        self.btnLenPotencia.setObjectName("btnLenPotencia")
        self.btnLenConcatenacion = QtWidgets.QPushButton(self.paginaLenguajes)
        self.btnLenConcatenacion.setGeometry(QtCore.QRect(520, 170, 131, 41))
        self.btnLenConcatenacion.setObjectName("btnLenConcatenacion")
        self.selecPotencia_2 = QtWidgets.QSpinBox(self.paginaLenguajes)
        self.selecPotencia_2.setGeometry(QtCore.QRect(270, 220, 101, 41))
        self.selecPotencia_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.selecPotencia_2.setObjectName("selecPotencia_2")
        self.label_2 = QtWidgets.QLabel(self.paginaLenguajes)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 91, 21))
        self.label_2.setStyleSheet("color: rgb(245, 121, 0);\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.paginaLenguajes)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 91, 21))
        self.label_3.setStyleSheet("color: rgb(245, 121, 0);\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.label_3.setObjectName("label_3")
        self.mostrarLenguaje1 = QtWidgets.QLineEdit(self.paginaLenguajes)
        self.mostrarLenguaje1.setGeometry(QtCore.QRect(130, 40, 531, 41))
        self.mostrarLenguaje1.setFrame(True)
        self.mostrarLenguaje1.setClearButtonEnabled(True)
        self.mostrarLenguaje1.setObjectName("mostrarLenguaje1")
        self.mostrarLenguaje2 = QtWidgets.QLineEdit(self.paginaLenguajes)
        self.mostrarLenguaje2.setGeometry(QtCore.QRect(130, 120, 531, 41))
        self.mostrarLenguaje2.setFrame(True)
        self.mostrarLenguaje2.setClearButtonEnabled(True)
        self.mostrarLenguaje2.setObjectName("mostrarLenguaje2")
        self.stackedWidget.addWidget(self.paginaLenguajes)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.paginas)
        self.verticalLayout.addWidget(self.inferior)

        self.retranslateUi(ventanaPrincipal)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "Alphabet"))
        self.btnMenu.setText(_translate("ventanaPrincipal", "Men??"))
        self.btnAlfabetos.setText(_translate("ventanaPrincipal", "Alfabetos"))
        self.btnLenguajes.setText(_translate("ventanaPrincipal", "Lenguajes"))
        self.pushButton_4.setText(_translate("ventanaPrincipal", "PushButton"))
        self.pushButton_5.setText(_translate("ventanaPrincipal", "PushButton"))
        self.pushButton_6.setText(_translate("ventanaPrincipal", "PushButton"))
        self.pushButton_8.setText(_translate("ventanaPrincipal", "Unimagdalena"))
        self.lineEditConjuntoA.setPlaceholderText(_translate("ventanaPrincipal", "ingrese alfabeto 1"))
        self.lineEditConjuntoB.setPlaceholderText(_translate("ventanaPrincipal", "ingrese alfabeto 2"))
        self.btnUnion.setText(_translate("ventanaPrincipal", "Uni??n"))
        self.btninterseccion.setText(_translate("ventanaPrincipal", "Intersecci??n"))
        self.btnDiferencia.setText(_translate("ventanaPrincipal", "Diferencia"))
        self.cerraduraEstrella.setText(_translate("ventanaPrincipal", "Cerradura"))
        self.selecPotencia_1.setToolTip(_translate("ventanaPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.crearLenguajes.setText(_translate("ventanaPrincipal", "Crear Lenguajes"))
        self.btnLenUnion.setText(_translate("ventanaPrincipal", "Union Lenguajes"))
        self.btnLenDiferencia.setText(_translate("ventanaPrincipal", "Diferencia Lenguajes"))
        self.btnLenInterseccion.setText(_translate("ventanaPrincipal", "Intersecci??n Lenguajes"))
        self.btnLenInvertir.setText(_translate("ventanaPrincipal", "Invertir Lenguajes"))
        self.btnLenCardinalidad.setText(_translate("ventanaPrincipal", "Cardinalidad Lenguajes"))
        self.btnLenPotencia.setText(_translate("ventanaPrincipal", "Potencia Lenguajes"))
        self.btnLenConcatenacion.setText(_translate("ventanaPrincipal", "Concatenaci??n Lenguajes"))
        self.selecPotencia_2.setToolTip(_translate("ventanaPrincipal", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("ventanaPrincipal", "Lenguaje 2"))
        self.label_3.setText(_translate("ventanaPrincipal", "Lenguaje 1"))
        self.mostrarLenguaje1.setPlaceholderText(_translate("ventanaPrincipal", "Lenguaje 1"))
        self.mostrarLenguaje2.setPlaceholderText(_translate("ventanaPrincipal", "Lenguaje 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaPrincipal = QtWidgets.QWidget()
    ui = Ui_ventanaPrincipal()
    ui.setupUi(ventanaPrincipal)
    ventanaPrincipal.show()
    sys.exit(app.exec_())
