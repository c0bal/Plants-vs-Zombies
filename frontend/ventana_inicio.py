from PyQt5.QtCore import pyqtSignal
from PyQt5 import uic
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_INICIO)

class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(str)
    senal_enviar_ranking = pyqtSignal()
    senal_enviar_usuario = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    
    def init_gui(self):
        self.setWindowTitle("Ventana de Inicio")
        self.button3.clicked.connect(self.close)
        self.button1.clicked.connect(self.enviar_login)
        self.button2.clicked.connect(self.enviar_ranking)
    
    def enviar_ranking(self):
        self.senal_enviar_ranking.emit()
        self.hide()

    def enviar_login(self):
        usuario = self.usuario_text.text()
        self.senal_enviar_usuario.emit(usuario)
        self.senal_enviar_login.emit(usuario)
    
    def recibir_validacion(self, validacion, errores):
    
        if validacion == True:
            self.hide()
        else:
            texto = 'Debe ser:'
            if 'alnum' in errores:
                texto += 'Alfanumerico/'
            if 'largo' in errores:
                texto += 'Largo:' + str(p.MIN_CARACTERES) + '-' + \
                    str(p.MAX_CARACTERES) + '/'
            if 'vacio' in errores:
                texto += 'No vacío'
            self.usuario_text.setText('')
            self.usuario_text.setPlaceholderText(texto)
        
        
    