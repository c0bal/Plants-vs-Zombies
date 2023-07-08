from PyQt5 import uic
import parametros as p
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal
from frontend.widgets_creados import PlantasTienda, LabelJardin, SolClickeable, PlantaReal, Guiso
from PyQt5.QtWidgets import QLabel
from aparicion_zombies import intervalo_aparicion
from PyQt5.QtTest import QTest

window_name, base_class = uic.loadUiType(p.RUTA_UI_JUEGO)

class VentanaJuego(window_name, base_class):
    senal_iniciar_juego = pyqtSignal(int, str)
    senal_plantar = pyqtSignal(int, int, int, str)
    senal_mate_planta = pyqtSignal()
    senal_agarrar_sol = pyqtSignal(int)
    senal_soles_creados = pyqtSignal()
    senal_plantas_cambiadas = pyqtSignal()
    senal_disparos_creados = pyqtSignal()
    senal_proyectiles_movidos = pyqtSignal()
    senal_proyectiles_eliminados = pyqtSignal()
    senal_cambie_proyectil = pyqtSignal()
    senal_movi_zombies = pyqtSignal()
    senal_mate_zombies = pyqtSignal()
    senal_pausar_juego = pyqtSignal()
    senal_reanudar_juego = pyqtSignal()
    senal_cheat_kill = pyqtSignal()
    senal_cheat_sun = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_avanzar_ronda = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.labels_plantas = {}
        self.labels_soles = {}
        self.labels_guisos = {}
        self.labels_zombies = {}
        self.ronda = 1
        self.estado_ventana = 'jugar'
        self.puede_plantar = False
        self.ruta_nueva_planta = ''
        self.ambiente = ''
        self.ponderador = ''
        self.pausa = False
        self.iniciado = False
        self.murio = False
        self.letras = []

    def init_gui(self):
        self.tienda = []
        self.setWindowTitle('Ventanana Juego')
        self.boton_girasol = PlantasTienda(QPixmap(p.RUTA_GIRASOL), self, 20, 20, p.RUTA_GIRASOL)
        self.boton_guisante = PlantasTienda(QPixmap(p.RUTA_GUISANTE), self, 20, 180, 
                                            p.RUTA_GUISANTE)
        self.boton_hielo = PlantasTienda(QPixmap(p.RUTA_HIELO), self, 20, 330, p.RUTA_HIELO)
        self.boton_papa = PlantasTienda(QPixmap(p.RUTA_PAPA), self, 20, 500, p.RUTA_PAPA)
        self.tienda.append(self.boton_girasol)
        self.tienda.append(self.boton_guisante)
        self.tienda.append(self.boton_hielo)
        self.tienda.append(self.boton_papa)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_iniciar.clicked.connect(self.iniciar)
        self.boton_pausar.clicked.connect(self.pausar)
        self.boton_avanzar.clicked.connect(self.avanzar)
        self.label_1 = LabelJardin('', self, 405, 200, 1)
        self.label_2 = LabelJardin('', self, 480, 200, 2)
        self.label_3 = LabelJardin('', self, 555, 200, 3)
        self.label_4 = LabelJardin('', self, 630, 200, 4)
        self.label_5 = LabelJardin('', self, 705, 200, 5)
        self.label_6 = LabelJardin('', self, 777, 200, 6)
        self.label_7 = LabelJardin('', self, 853, 200, 7)
        self.label_8 = LabelJardin('', self, 927, 200, 8)
        self.label_9 = LabelJardin('', self, 1003, 200, 9)
        self.label_10 = LabelJardin('', self, 1074, 200, 10)
        self.label_11 = LabelJardin('', self, 405, 302, 11)
        self.label_12 = LabelJardin('', self, 480, 302, 12)
        self.label_13 = LabelJardin('', self, 555, 302, 13)
        self.label_14 = LabelJardin('', self, 630, 302, 14)
        self.label_15 = LabelJardin('', self, 705, 302, 15)
        self.label_16 = LabelJardin('', self, 777, 302, 16)
        self.label_17 = LabelJardin('', self, 853, 302, 17)
        self.label_18 = LabelJardin('', self, 927, 302, 18)
        self.label_19 = LabelJardin('', self, 1003, 302, 19)
        self.label_20 = LabelJardin('', self, 1074, 302, 20)

    def salir(self):
        self.senal_salir.emit()
    def avanzar(self):
        if self.pausa == False:
            if int(self.soles_text.text()) >= p.COSTO_AVANZAR:
                self.senal_avanzar_ronda.emit()
            
    def esconder_objetos(self):
        for i in self.labels_zombies:
            self.labels_zombies[i].hide()
        for i in self.labels_soles:
            self.labels_soles[i].hide()
        for i in self.labels_guisos:
            self.labels_guisos[i].hide()    
    def mostrar_salvado(self):
        self.crazy_cruz_grande = QLabel(self)
        self.crazy_cruz_grande.setGeometry(310, 260, 441, 321)
        self.crazy_cruz_grande.setMaximumSize(441, 321)
        pixels = QPixmap(p.RUTA_CRAZY)
        self.crazy_cruz_grande.setPixmap(pixels)
        self.crazy_cruz_grande.setScaledContents(True)
        self.crazy_cruz_grande.show()
        self.crazy_cruz.hide()
        self.salvado.show() 
        QTest.qWait(2000)
        self.crazy_cruz_grande.hide()
        self.salvado.hide()

    def pausar(self):
        if self.pausa == False:
            self.estado_ventana = 'pausa'
            self.senal_pausar_juego.emit()
            self.boton_pausar.setStyleSheet('background: rgb(200,0,0);')
            self.boton_iniciar.setStyleSheet('background-color: lightgreen;')
            self.boton_avanzar.setStyleSheet('background-color: lightgreen;')
            for i in self.tienda:
                i.setStyleSheet('background-color: lightgreen;')
            self.pausa = True
        else:
            self.estado_ventana = 'jugar'
            self.boton_pausar.setStyleSheet('background: rgb(0,170,0);')
            self.boton_iniciar.setStyleSheet('background: rgb(0,170,0);')
            self.boton_avanzar.setStyleSheet('background: rgb(0,170,0);')
            for i in self.tienda:
                i.setStyleSheet('background: rgb(0,170,0);')
            self.pausa = False
            self.senal_reanudar_juego.emit()
            if self.iniciado == True:
                self.boton_iniciar.setStyleSheet('background-color: lightgreen;')
    def iniciar(self):
        if self.pausa == False and self.iniciado == False:
            self.iniciado = True
            self.boton_iniciar.setStyleSheet('background-color: lightgreen;')
            self.puede_plantar = False
            aparicion_zombies = int(intervalo_aparicion(self.ronda, self.ponderador)*5000)         
            self.senal_iniciar_juego.emit(aparicion_zombies, self.ambiente)
    def abrir(self, ambiente, ronda):
        self.ambiente = ambiente
        self.ronda = ronda
        self.crazy_cruz.show()
        if ambiente == 'noche':
            self.ponderador = p.PONDERADOR_NOCTURNO
            self.fondo.setPixmap(QPixmap(p.RUTA_FONDO_NOCHE))
        else:
            self.ponderador = p.PONDERADOR_DIURNO
            self.fondo.setPixmap(QPixmap(p.RUTA_FONDO_DIA))
        self.salvado.hide()
        self.show()
    def setear_datos(self, datos: dict):
        self.soles_text.setText(str(datos['Soles']))
        self.soles_text.repaint()
        self.nivel_text.setText(str(datos['Nivel']))
        self.nivel_text.repaint()
        self.puntaje_text.setText(str(datos['Puntaje']))
        self.puntaje_text.repaint()
        self.zombies_muertos_text.setText(str(datos['Zombies Muertos']))
        self.zombies_muertos_text.repaint()
        self.zombies_vivos_text.setText(str(datos['Zombies Restantes']))
        self.zombies_vivos_text.repaint()
    
    def crear_proyectil(self, dic):
        for i in dic:
            self.labels_guisos[i] = Guiso(self, dic[i][2], dic[i][0], dic[i][1])
            pixmap = QPixmap(dic[i][3])
            self.labels_guisos[i].setPixmap(pixmap)
            self.labels_guisos[i].show()
        self.senal_disparos_creados.emit()
    
    def eliminar_proyectiles(self, dic):
        for i in dic:
            self.labels_guisos[i].hide()
            del self.labels_guisos[i]
        self.senal_proyectiles_eliminados.emit()
    
    def mover_proyectiles(self, dic):
        for i in dic:
            self.labels_guisos[i].move(dic[i][0], dic[i][1])
        self.senal_proyectiles_movidos.emit()

    def cambiar_proyectil(self, dic):
        for i in dic:
            pixmap = QPixmap(dic[i])
            self.labels_guisos[i].setPixmap(pixmap)
        self.senal_cambie_proyectil.emit()

    def cambiar_imagen_plantas(self, dict):
        for i in dict:
            pixmap = QPixmap(dict[i])
            self.labels_plantas[i].setPixmap(pixmap)
        self.senal_plantas_cambiadas.emit()
    
    def eliminar_planta(self, dict):
        for i in dict:
            self.labels_plantas[i].hide()
            del self.labels_plantas[i]
        self.senal_mate_planta.emit()

    def crear_zombie(self, lista1, lista2):
        z = QLabel(self)
        z.setGeometry(lista1[0], lista1[1], 71, 101)
        z.setMaximumSize(71, 101)
        
        pixels = QPixmap(lista1[3])
        z.setPixmap(pixels)
        z.setScaledContents(True)
        self.labels_zombies[lista1[2]] = z
        z.show()
        
        z2 = QLabel(self)
        z2.setGeometry(lista2[0], lista2[1], 71, 101)
        z2.setMaximumSize(71, 101)
        
        pixels2 = QPixmap(lista2[3])
        z2.setPixmap(pixels2)
        z2.setScaledContents(True)
        self.labels_zombies[lista2[2]] = z2
        z2.show()
    
    def eliminar_zombies(self, dic):
        for i in dic:
            self.labels_zombies[i].hide()
            del self.labels_zombies[i]
        self.senal_mate_zombies.emit()
    
    def cambiar_imagen_zombie(self, dic):
        for i in dic:
            self.labels_zombies[i].move(int(dic[i][0]), int(dic[i][1]))
            pixmap = QPixmap(dic[i][2])
            self.labels_zombies[i].setPixmap(pixmap)
        self.senal_movi_zombies.emit()

    def crear_sol(self, dic):
        for i in dic:
            sol = SolClickeable(self)
            sol.numero_id = dic[i][2]
            sol.setGeometry(dic[i][0], dic[i][1], 50, 50)
            sol.setMaximumSize(50, 50)

            pixels = QPixmap(p.RUTA_SOL)
            sol.setPixmap(pixels)
            sol.setScaledContents(True)
            self.labels_soles[dic[i][2]] = sol
            sol.show()
        self.senal_soles_creados.emit()
    
    def agarrar_sol(self, numero):
        self.labels_soles[numero].hide()
        del self.labels_soles[numero]
        self.senal_agarrar_sol.emit(numero)
    
    def crear_planta(self, numero, x, y):
        planta = PlantaReal(self)
        planta.numero_identificador = numero
        planta.setGeometry(x, y, 70, 100)
        planta.setMaximumSize(70, 100)

        pixels = QPixmap(self.ruta_nueva_planta)
        planta.setPixmap(pixels)
        planta.setScaledContents(True)
        self.labels_plantas[numero] = planta
        planta.show()
        self.puede_plantar = False
        
        if self.ruta_nueva_planta in p.RUTA_GUISANTE:
            planta.tipo = 'lanzaguisantes'   
        elif self.ruta_nueva_planta in p.RUTA_HIELO:
            planta.tipo = 'lanzaguisantesHielo'
        elif self.ruta_nueva_planta in p.RUTA_GIRASOL:
            planta.tipo = 'girasol'
        else:
            planta.tipo = 'patata'

        self.senal_plantar.emit(numero, x, y, planta.tipo)
        
    def ruta_a_plantar(self, ruta):
        if self.estado_ventana != 'pausa':
            self.ruta_nueva_planta = ruta
            plata_restante = int(self.soles_text.text())
            if self.ruta_nueva_planta in p.RUTA_GUISANTE:
                plata_restante -= 100  
            elif self.ruta_nueva_planta in p.RUTA_HIELO:
                plata_restante -= 150
            elif self.ruta_nueva_planta in p.RUTA_GIRASOL:
                plata_restante -= 50
            else:
                plata_restante -= 75
            
            if plata_restante >= 0:
                self.puede_plantar = True

    def reset(self):
        for i in self.labels_plantas:
            self.labels_plantas[i].hide()
        self.labels_plantas = {}
        self.labels_soles = {}
        self.labels_guisos = {}
        self.labels_zombies = {}

        self.salvado.hide()
        
        self.letras = []
        self.estado_ventana = 'jugar'
        self.puede_plantar = False
        self.ruta_nueva_planta = ''
        self.pausa = False
        self.iniciado = False
        self.murio = False

        self.soles_text.setText(str(p.SOLES_INICIALES))
        self.soles_text.repaint()
        self.nivel_text.setText(str(0))
        self.nivel_text.repaint()
        self.puntaje_text.setText(str(0))
        self.puntaje_text.repaint()
        self.zombies_muertos_text.setText(str(0))
        self.zombies_muertos_text.repaint()
        self.zombies_vivos_text.setText(str(2*p.N_ZOMBIES))
        self.zombies_vivos_text.repaint()

    def cerrar(self):
        self.hide()

    def siguiente_ronda(self, ambiente, ronda):
        self.ambiente = ambiente
        self.ronda = ronda
        self.crazy_cruz.show()
        self.boton_iniciar.setStyleSheet('background: rgb(0,170,0);')
        if ambiente == 'noche':
            self.ponderador = p.PONDERADOR_NOCTURNO
            self.fondo.setPixmap(QPixmap(p.RUTA_FONDO_NOCHE))
        else:
            self.ponderador = p.PONDERADOR_DIURNO
            self.fondo.setPixmap(QPixmap(p.RUTA_FONDO_DIA)) 
        self.show() 

    def te_mataron(self):
        self.murio = True
        self.muerte_gigante = QLabel(self)
        self.muerte_gigante.setGeometry(490, 100, 620, 390)
        pixels = QPixmap(p.RUTA_MUERTE)
        self.muerte_gigante.setPixmap(pixels)
        self.muerte_gigante.setScaledContents(True)
        self.muerte_gigante.show()
        self.crazy_cruz.hide()
        self.salvado.hide()
        QTest.qWait(2000)
        self.muerte_gigante.hide()
    def keyPressEvent(self, event):
        letra = event.text().lower()
        if letra == 'p':
            return self.pausar()
        if len(self.letras) == 1:
            if self.letras[0] == 'k':
                if letra.lower() == 'i':
                    self.letras.append('i')
                elif letra.lower() == 'k':
                    pass
                elif letra.lower() == 's':
                    self.letras = ['s']
                else:
                    self.letras = []
            elif self.letras[0] == 's':
                if letra.lower() == 'u':
                    self.letras.append('u')
                elif letra.lower() == 's':
                    pass
                elif letra.lower() == 'k':
                    self.letras = ['k']
                else:
                    self.letras = []
        elif len(self.letras) == 2:
            if self.letras[1] == 'i':
                if letra.lower() == 'l':
                    self.senal_cheat_kill.emit() 
                    self.letras = []
                else:
                    self.letras = []
            elif self.letras[1] == 'u':
                if letra.lower() == 'n':
                    self.senal_cheat_sun.emit()
                    self.letras = []
                else:
                    self.letras = []
        
        elif len(self.letras) == 0:
            if letra.lower() == 'k':
                self.letras.append('k')
            elif letra.lower() == 's':
                self.letras.append('s')
            else:
                self.letras = []