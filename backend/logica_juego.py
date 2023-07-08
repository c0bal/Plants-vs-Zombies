from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from backend.elementos_juego import PlantaClasica, PlantaAzul, PlantaPatata, \
                                PlantaGirasol, ZombieClasico, ZombieRapido, Soles
import parametros as p
from random import choice, randint
from PyQt5.QtTest import QTest

class LogicaJuego(QObject):
    senal_mover_planta = pyqtSignal(int, int)
    senal_cambiar_foto_plantas = pyqtSignal(dict)
    senal_eliminar_planta = pyqtSignal(dict)
    senal_cambiar_foto_zombie = pyqtSignal(dict)
    senal_crear_proyectil = pyqtSignal(dict)
    senal_eliminar_proyectil = pyqtSignal(dict)
    senal_cambiar_proyectil = pyqtSignal(dict)
    senal_mover_proyectiles = pyqtSignal(dict)
    senal_crear_zombie = pyqtSignal(list, list)
    senal_eliminar_zombie = pyqtSignal(dict)
    senal_crear_soles = pyqtSignal(dict)
    senal_actualizar_juego = pyqtSignal(dict)
    senal_cargar_datos_iniciales = pyqtSignal(str, int)
    senal_terminar_ronda = pyqtSignal(dict, bool)
    senal_cerrar_ventana_juego = pyqtSignal()
    senal_reset_ventana_juego = pyqtSignal()
    senal_salvado_zombies = pyqtSignal()
    senal_esconder_objetos_fin = pyqtSignal()
    senal_siguiente_ronda = pyqtSignal(str, int)
    senal_te_mataron = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.salir = False
        self.cheat_kill = False
        self.soles_pausados = False
        self.todos_eliminados = False
        self.zombies_creados = p.N_ZOMBIES
        self.puntaje_extra = 0
        self.timer_actualizar_datos = QTimer()
        self.ronda = ''
        self.datos_jugador = {'Soles': p.SOLES_INICIALES,
                    'Nivel': 1,
                    'Puntaje': 0,
                    'Zombies Muertos': 0,
                    'Zombies Restantes': 2*p.N_ZOMBIES}
        self.estado_juego = 'previa'
        self.plantas = {}
        self.soles = {}
        self.guisos = {}
        self.zombies = {}
        self.plantas_que_cambian = {}
        self.plantas_a_eliminar = {}
        self.disparos_que_se_crean = {}
        self.proyectiles_a_mover = {}
        self.proyectiles_a_eliminar = {}
        self.proyectiles_a_cambiar = {}
        self.soles_creados = {}
        self.numero_identificador_guiso = 0
        self.numero_identificador_sol = 0
        self.numero_identificador_zombie = 0
        self.timer_soles = QTimer()
        self.zombies_que_cambian = {}
        self.zombies_a_eliminar = {}
        self.timer_crear_zombies = QTimer()
        self.configurar_timer()

    def poner_planta(self, numero, x, y, tipo):
        if tipo == 'lanzaguisantes':
            self.plantas[numero] = PlantaClasica(x, y, numero, self)
            if self.estado_juego == 'jugando':
                self.plantas[numero].timer_disparo.start()
        elif tipo == 'lanzaguisantesHielo':
            self.plantas[numero] = PlantaAzul(x, y, numero, self)
            if self.estado_juego == 'jugando':
                self.plantas[numero].timer_disparo.start() 
        elif tipo == 'girasol':
            self.plantas[numero] = PlantaGirasol(x, y, numero, self)
            if self.estado_juego == 'jugando':
                self.plantas[numero].timer_disparo.start() 
        else:
            self.plantas[numero] = PlantaPatata(x, y, numero, self) 
        self.datos_jugador['Soles'] -= self.plantas[numero].costo
    
    def configurar_timer(self):
        self.timer_actualizar_datos.setInterval(40)
        self.timer_actualizar_datos.timeout.connect(self.actualizar_juego)
        self.timer_soles.setInterval(p.INTERVALO_SOLES_GIRASOL)
        self.timer_soles.timeout.connect(self.sol_random)

    def actualizar_juego(self):
        self.senal_actualizar_juego.emit(self.datos_jugador)
        self.senal_mover_proyectiles.emit(self.proyectiles_a_mover)
        self.senal_cambiar_foto_plantas.emit(self.plantas_que_cambian)
        self.senal_crear_proyectil.emit(self.disparos_que_se_crean)
        self.senal_crear_soles.emit(self.soles_creados)
        self.senal_cambiar_foto_zombie.emit(self.zombies_que_cambian)
        self.senal_eliminar_zombie.emit(self.zombies_a_eliminar)
        self.senal_eliminar_planta.emit(self.plantas_a_eliminar)
        self.senal_cambiar_proyectil.emit(self.proyectiles_a_cambiar)
        self.senal_eliminar_proyectil.emit(self.proyectiles_a_eliminar)

    def eliminar_proyectiles_movidos(self):
        self.proyectiles_a_mover = {}
    def eliminar_proyectiles_eliminados(self):      
        self.proyectiles_a_eliminar = {}
    def eliminiar_disparos_creados(self):
        self.disparos_que_se_crean = {}    
    def eliminar_plantas_cambiados(self):
        self.plantas_que_cambian = {}
    def eliminar_soles_creados(self):
        self.soles_creados = {}
    def eliminar_zombies_movidos(self):
        self.zombies_que_cambian = {}
    def eliminar_zombies_eliminados(self):
        self.zombies_a_eliminar = {}
    def eliminar_plantas_eliminadas(self):
        self.plantas_a_eliminar = {}

    def sol_random(self):
        x = randint(200, 1100)
        y = randint(50, 500)
        sol = Soles(y, x, self)
        self.crear_soles(sol)

    def crear_soles(self, sol):
        sol.numero_id = self.numero_identificador_sol
        self.numero_identificador_sol += 1
        self.soles_creados[sol.numero_id] = [sol.x, sol.y, sol.numero_id]
        self.soles[sol.numero_id] = sol

    def crear_zombie(self):
        if self.zombies_creados > 0:
            z11 = ZombieClasico(1, 1160, 200, self)
            z12 = ZombieClasico(2, 1160, 302, self)
            z21 = ZombieRapido(1, 1160, 200, self)
            z22 = ZombieRapido(2, 1160, 302, self)
            zombie = choice([z11, z21])
            zombie2 = choice([z12, z22])
            self.zombies[self.numero_identificador_zombie] = zombie
            zombie.numero_id = self.numero_identificador_zombie
            self.numero_identificador_zombie += 1
            self.zombies[self.numero_identificador_zombie] = zombie2
            zombie2.numero_id = self.numero_identificador_zombie
            self.numero_identificador_zombie += 1
            self.senal_crear_zombie.emit([zombie.x, zombie.y, zombie.numero_id, zombie.ruta],
                                        [zombie2.x, zombie2.y, zombie2.numero_id, zombie2.ruta])
            zombie.timer_moverse.start()
            zombie2.timer_moverse.start()
            self.zombies_creados -= 1
        else:
            self.timer_crear_zombies.stop()
            
    def crear_proyectil_guisante(self, guiso): 
        if guiso.tipo == 'lanzaguisantes':
            guiso.numero_id = self.numero_identificador_guiso
            self.numero_identificador_guiso += 1
            self.disparos_que_se_crean[guiso.numero_id] = [guiso.x, guiso.y, guiso.numero_id, 
                                                        p.RUTA_PROYECTIL_VERDE]
            self.guisos[guiso.numero_id] = guiso
        elif guiso.tipo == 'lanzaguisantesHielo':
            guiso.numero_id = self.numero_identificador_guiso
            guiso.realentizador = True
            self.numero_identificador_guiso += 1
            self.disparos_que_se_crean[guiso.numero_id] = [guiso.x, guiso.y, guiso.numero_id,
                                                         p.RUTA_PROYECTIL_AZUL]  
            self.guisos[guiso.numero_id] = guiso

    def eliminar_zombie(self, numero, llego):
        for i in self.plantas:
            planta = self.plantas[i]
            for z in planta.zombies_comiendosela:
                if z.numero_id == numero:
                    planta.zombies_comiendosela.remove(z)
        del self.zombies[numero]
        self.zombies_a_eliminar[numero] = ''

        self.datos_jugador['Puntaje'] += self.puntaje_matar_zombie
        self.datos_jugador['Zombies Muertos'] += 1
        if self.datos_jugador['Zombies Restantes'] == 1:
            self.datos_jugador['Zombies Restantes'] -= 1
            self.todos_eliminados = True
            self.puntaje_extra = self.datos_jugador['Puntaje'] * self.ponderador_dificultad
            self.terminar_ronda()
        else:
            self.datos_jugador['Zombies Restantes'] -= 1

    def eliminar_planta(self, numero):
        for zombie in self.plantas[numero].zombies_comiendosela:
            zombie.timer_comiendo.stop()
            zombie.timer_moverse.start()
        del self.plantas[numero]
        self.plantas_a_eliminar[numero] = ''

    def mover_proyectiles(self, numero, pos):
        self.proyectiles_a_mover[numero] = pos
        
        for i in self.zombies:
            zombie = self.zombies[i]
            choque = self.zombies[i].revisar_choque(pos)
            if choque:
                if zombie.realentizado == False:
                    zombie.velocidad = zombie.velocidad*(1-p.RALENTIZAR_ZOMBIE)
                    zombie.realentizado = True
                self.guisos[numero].timer_moverse.stop()
                self.guisos[numero].timer_animacion.start()
                return self.bajar_vida_zombie(zombie, self.guisos[numero].dano)

    def bajar_vida_zombie(self, zombie, dano):
        zombie.vida -= dano

    def mover_zombies(self, numero, lista):
        self.zombies_que_cambian[numero] = lista
        for i in self.plantas:
            planta = self.plantas[i]
            choque = self.plantas[i].revisar_choque(lista)
            if choque:
                return self.planta_chocada(planta, numero)
        if self.zombies[numero].llego_fin == True:
            self.terminar_ronda()
                
    def planta_chocada(self, planta, numero):
        self.zombies[numero].estado = 'comiendo'
        planta.zombies_comiendosela.append(self.zombies[numero])
        self.zombies[numero].timer_moverse.stop()
        self.zombies[numero].timer_comiendo.start()

    def zombie_comer(self, numero, lista):
        self.zombies_que_cambian[numero] = lista
        for i in self.plantas:
            planta = self.plantas[i]
            zombie = self.zombies[numero]
            if zombie in planta.zombies_comiendosela:
                return self.bajar_vida_planta(planta, zombie.dano)

    def bajar_vida_planta(self, planta, dano):
        planta.vida -= dano
    def zombie_cambiar_foto(self, numero, lista):
        self.zombies_que_cambian[numero] = lista
    def planta_cambiar(self, numero, ruta):
        self.plantas_que_cambian[numero] = ruta
    def cambiar_imagen_guiso(self, numero, ruta):
        self.proyectiles_a_cambiar[numero] = ruta
    def eliminar_proyectiles_a_cambiar(self):      
        self.proyectiles_a_cambiar = {}
    def iniciar(self, intervalo_zombies, ambiente):
        self.estado_juego = 'jugando'
        self.intervalo_zombies = intervalo_zombies
        self.ambiente = ambiente
        self.timer_crear_zombies.setInterval(intervalo_zombies)
        self.timer_crear_zombies.timeout.connect(self.crear_zombie)
        self.timer_crear_zombies.start()
        if self.ambiente == 'dia':
            self.timer_soles.start()
        if len(self.plantas) > 0:
            for i in self.plantas:
                if self.plantas[i].tipo != 'patata':
                    self.plantas[i].timer_disparo.start()
    def agarrar_sol(self, numero):
        del self.soles[numero]
        self.datos_jugador['Soles'] += 2 * p.SOLES_POR_RECOLECCION
    def apertura(self, ambiente, ronda):
        self.ambiente = ambiente
        self.ronda = ronda
        if self.ambiente == 'dia':
            self.ponderador_dificultad = p.PONDERADOR_DIURNO
            self.puntaje_matar_zombie = p.PUNTAJE_ZOMBIE_DIURNO
        else:
            self.ponderador_dificultad = p.PONDERADOR_NOCTURNO
            self.puntaje_matar_zombie = p.PUNTAJE_ZOMBIE_NOCTURNO

        self.senal_cargar_datos_iniciales.emit(self.ambiente, self.ronda)
        self.timer_actualizar_datos.start()
    
    def reset_datos(self):
        self.salir = False
        self.todos_eliminados = False
        self.zombies_creados = p.N_ZOMBIES
        self.puntaje_extra = 0
        self.datos_jugador = {'Soles': p.SOLES_INICIALES,
                    'Nivel': self.ronda,
                    'Puntaje': 0,
                    'Zombies Muertos': 0,
                    'Zombies Restantes': 2*p.N_ZOMBIES}
        self.estado_juego = 'previa'
        self.plantas = {}
        self.soles = {}
        self.guisos = {}
        self.zombies = {}       
        self.plantas_que_cambian = {}
        self.plantas_a_eliminar = {}
        self.disparos_que_se_crean = {}
        self.proyectiles_a_mover = {}
        self.proyectiles_a_eliminar = {}
        self.proyectiles_a_cambiar = {}
        self.soles_creados = {}
        self.numero_identificador_guiso = 0
        self.numero_identificador_sol = 0
        self.numero_identificador_zombie = 0
        self.zombies_que_cambian = {}
        self.zombies_a_eliminar = {}  
        self.senal_reset_ventana_juego.emit()  
        self.cheat_kill = False
    def pausar(self):
        if self.timer_actualizar_datos.isActive():
            self.timer_actualizar_datos.stop()
        if self.timer_crear_zombies.isActive():
            self.timer_crear_zombies.stop()
        if self.timer_soles.isActive():
            self.soles_pausados = True
            self.timer_soles.stop()
        for i in self.zombies:
            if self.zombies[i].timer_moverse.isActive():
                self.zombies[i].timer_moverse_pausado = True
                self.zombies[i].timer_moverse.stop()
            elif self.zombies[i].timer_comiendo.isActive():
                self.zombies[i].timer_comiendo.stop()
                self.zombies[i].timer_comer_pausada = True
        for i in self.plantas:
            if self.plantas[i].tipo != 'patata':
                if self.plantas[i].timer_disparo.isActive():
                    self.plantas[i].timer_disparo.stop()
                    self.plantas[i].timer_disparo_pausado = True
        for i in self.guisos:
            if self.guisos[i].timer_moverse.isActive():
                self.guisos[i].timer_moverse.stop()
                self.guisos[i].timer_moverse_pausado = True
            elif self.guisos[i].timer_animacion.isActive():
                self.guisos[i].timer_animacion_pausada = True
                self.guisos[i].timer_animacion.stop()

    def reanudar(self):
        self.timer_actualizar_datos.start()
        if self.zombies_creados > 0:
            self.timer_crear_zombies.start()
        if self.soles_pausados:
            self.timer_soles.start()
            self.soles_pausados = False
        for i in self.zombies:
            if self.zombies[i].timer_moverse_pausado:
                self.zombies[i].timer_moverse_pausado = False
                self.zombies[i].timer_moverse.start()
            elif self.zombies[i].timer_comer_pausada:
                self.zombies[i].timer_comer_pausada = False
                self.zombies[i].timer_comiendo.start()
        for i in self.plantas:
            if self.plantas[i].tipo != 'patata':
                if self.plantas[i].timer_disparo_pausado:
                    self.plantas[i].timer_disparo.start()
                    self.plantas[i].timer_disparo_pausado = False
        for i in self.guisos:
            if self.guisos[i].timer_moverse_pausado:
                self.guisos[i].timer_moverse_pausado = False
                self.guisos[i].timer_moverse.start()
            if self.guisos[i].timer_animacion_pausada:
                self.guisos[i].timer_animacion.start()
                self.guisos[i].timer_animacion_pausada = False
    def salir_ronda(self):
        self.salir = True
        self.terminar_ronda()
    def terminar_ronda(self):
        self.pausar()
        self.senal_actualizar_juego.emit(self.datos_jugador)
        self.senal_esconder_objetos_fin.emit()
        if self.salir == False:
            if self.todos_eliminados == True:
                self.senal_salvado_zombies.emit()
            else:
                self.senal_te_mataron.emit()
        QTest.qWait(4000)
        puntaje_ronda = self.datos_jugador['Puntaje'] + self.puntaje_extra        
        self.senal_terminar_ronda.emit({'Ronda Actual': self.datos_jugador['Nivel'],
                                        'Soles Restantes': self.datos_jugador['Soles'],
                                        'Zombies Muertos': self.datos_jugador['Zombies Muertos'],
                                        'Puntaje Ronda': puntaje_ronda}, self.todos_eliminados)
        self.reset_datos()
        self.senal_cerrar_ventana_juego.emit()         
    def crear_proyectil_a_eliminar(self, numero):
        self.proyectiles_a_eliminar[numero] = ''
    def siguiente_ronda(self, datos):
        self.datos_jugador['Nivel'] = datos['Ronda Actual']
        self.senal_siguiente_ronda.emit(self.ambiente, datos['Ronda Actual'])
        self.timer_actualizar_datos.start()  
    def kill_all(self):
        self.cheat_kill = True
        self.todos_eliminados = True
        self.datos_jugador['Puntaje'] = 2*(p.N_ZOMBIES)*self.puntaje_matar_zombie
        self.datos_jugador['Zombies Restantes'] = 0
        self.datos_jugador['Zombies Muertos'] = 2*p.N_ZOMBIES
        self.terminar_ronda()
    def soles_extra(self):
        self.datos_jugador['Soles'] += p.SOLES_EXTRA
    def avanzar(self):
        self.todos_eliminados = True
        self.datos_jugador['Soles'] -= p.COSTO_AVANZAR
        self.terminar_ronda()