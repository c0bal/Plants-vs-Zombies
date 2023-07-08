from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal()

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario):
    
        errores = set()
        validacion = True

        if usuario.isalnum() == False:
            errores.add('alnum')
            validacion = False
        if usuario == '':
            errores.add('vacio')
            validacion = False
        if (len(usuario) >= p.MIN_CARACTERES and len(usuario) <= p.MAX_CARACTERES) == False:
            errores.add('largo')
            validacion = False

        if validacion == True:
            self.senal_abrir_juego.emit()
            pass
        
        self.senal_respuesta_validacion.emit(validacion, errores)