from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_RANKING)

class VentanaRanking(window_name, base_class):

    senal_salir_raking = pyqtSignal()
    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana Ranking")
        self.boton_volver.clicked.connect(self.volver_inicio)

    def volver_inicio(self):
        self.senal_volver_inicio.emit()
        self.hide()

    def abrir(self, datos: list):
        self.usuario1.setText(datos[0][0])
        self.puntaje1.setText(str(datos[0][1]))
        self.usuario2.setText(datos[1][0])
        self.puntaje2.setText(str(datos[1][1]))
        self.usuario3.setText(datos[2][0])
        self.puntaje3.setText(str(datos[2][1]))
        self.usuario4.setText(datos[3][0])
        self.puntaje4.setText(str(datos[3][1]))
        self.usuario5.setText(datos[4][0])
        self.puntaje5.setText(str(datos[4][1]))
        self.show()
    
    
        