from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class Guiso(QLabel):
    def __init__(self, parent, numero, x, y):
        super(Guiso, self).__init__(parent)
        self.setGeometry(x, y, 30, 30)
        self.setScaledContents(True)
        self.numero_id = numero
        self.parent = parent

class SolClickeable(QLabel):
    def __init__(self, parent):
        super(SolClickeable, self).__init__(parent)
        self.numero_id = ''
        self.parent = parent

    def mousePressEvent(self, evento):
        if evento.buttons() == Qt.RightButton and self.parent.pausa == False:
            self.parent.agarrar_sol(self.numero_id)

class PlantaReal(QLabel):
    def __init__(self, parent):
        super(PlantaReal, self).__init__(parent)
        self.numero_identificador = ''
        self.tipo = ''
        self.parent = parent


class PlantasTienda(QLabel):
    def __init__(self, pixmap, parent, x, y, ruta):
        super().__init__(parent)
        self.setGeometry(x, y, 80, 80)
        self.pixmap = pixmap
        self.setPixmap(self.pixmap)
        self.setStyleSheet('background: rgb(0,200,0);')
        self.setScaledContents(True)
        self.resize(100,100)
        self.parent = parent
        self.ruta = ruta
    
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.parent.ruta_a_plantar(self.ruta)

class LabelJardin(QLabel):
    def __init__(self, label, parent, x, y, pos):
        super().__init__(label, parent)
        self.setGeometry(x, y, 70, 100)
        self.setMaximumSize(70, 100)
        self.setAcceptDrops(True)
        self.parent = parent
        self.posicion = pos
        self.x = x
        self.y = y
        self.imagen = False
        self.tipo = ''
    
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton and self.parent.puede_plantar == True:
            self.parent.crear_planta(self.posicion, self.x, self.y)
        