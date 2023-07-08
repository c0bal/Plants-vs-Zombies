from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_PRINCIPAL)

class VentanaPrincipal(window_name, base_class):

    senal_ingresar_juego = pyqtSignal(str, int)
    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana Principal")
        self.boton_ingresar.clicked.connect(self.ingresar)
    
    def ingresar(self):
   
        if self.boton_dia.isChecked() == True:
            self.senal_ingresar_juego.emit('dia', 1)
            self.hide()
        
        elif self.boton_noche.isChecked() == True:
            self.senal_ingresar_juego.emit('noche', 1)
            self.hide()

    def mostrar_ventana(self):
        self.show()