from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_POST)

class VentanaPost(window_name, base_class):
    
    senal_siguiente_ronda = pyqtSignal(dict)
    senal_cargar_datos = pyqtSignal(int)
    senal_abrir_inicio = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.datos = {}
        self.puntaje_total = 0
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana Post-ronda")
        self.boton_siguiente.clicked.connect(self.siguiente_ronda)
        self.boton_salir.clicked.connect(self.salir)

    def abrir(self, datos, paso):
        self.datos = datos
        self.puntaje_total += datos['Puntaje Ronda']
        self.ronda_actual_text.setText(str(datos['Ronda Actual']))
        self.soles_restantes_text.setText(str(datos['Soles Restantes']))
        self.zombies_destruidos_text.setText(str(datos['Zombies Muertos']))
        self.puntaje_ronda_text.setText(str(datos['Puntaje Ronda']))
        self.puntaje_total_text.setText(str(self.puntaje_total))
        self.show()
        self.label_mensaje_bien.show()
        if paso == False:
            self.label_mensaje_bien.hide()
            self.boton_siguiente.hide()
        else:
            self.label_mensaje_mal.hide()
    
    def siguiente_ronda(self):
        self.datos['Ronda Actual'] += 1
        self.senal_siguiente_ronda.emit(self.datos)
        self.hide()
    
    def salir(self):
        self.senal_cargar_datos.emit(self.puntaje_total)
        self.senal_abrir_inicio.emit()
        self.close()

    

    

    