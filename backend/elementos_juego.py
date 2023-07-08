from PyQt5.QtCore import QObject, QTimer
import parametros as p
from random import choice

class Proyectil(QObject):
    def __init__(self, pos_x, pos_y, tipo, parent):
        super().__init__()
        self.y = pos_y
        self._x = pos_x
        self.velocidad = p.VELOCIDAD_GUISO
        self.active = True
        self.tipo = tipo
        self.dano = p.DANO_PROYECTIL
        self.realentizador = False
        self.numero_id = ''
        self.foto = 0
        self.rutav1 = p.RUTA_PROYECTIL_VERDEB
        self.rutav2 = p.RUTA_PROYECTIL_VERDEC
        self.rutaa1 = p.RUTA_PROYECTIL_AZULB
        self.rutaa2 = p.RUTA_PROYECTIL_AZULC
        self.parent = parent
        self.timer_animacion_pausada = False
        self.timer_moverse_pausado = False
        self.timer_moverse = QTimer()
        self.timer_animacion = QTimer()
        self.configurar_timer()
   
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        if valor >= p.LIMITE_DERECHA + 100:
            self.eliminar() 
        else:
            self._x = valor
    
    def configurar_timer(self):
        self.timer_moverse.setInterval(35)
        self.timer_moverse.timeout.connect(self.enviar_movimiento)
        self.timer_animacion.setInterval(20)
        self.timer_animacion.timeout.connect(self.animacion)

    def animacion(self):
        if self.foto == 0:
            if self.tipo == 'lanzaguisantes':
                self.parent.cambiar_imagen_guiso(self.numero_id, self.rutav1)
            else:
                self.parent.cambiar_imagen_guiso(self.numero_id, self.rutaa1)
            self.foto += 1
        
        elif self.foto == 1:
            if self.tipo == 'lanzaguisantes':
                self.parent.cambiar_imagen_guiso(self.numero_id, self.rutav2)
            else:
                self.parent.cambiar_imagen_guiso(self.numero_id, self.rutaa2)
            self.foto += 1   

        elif self.foto == 2:    
                self.foto = 0
                self.eliminar()
                self.timer_animacion.stop()

    def eliminar(self):
        self.parent.crear_proyectil_a_eliminar(self.numero_id)
        self.active = False
        if self.timer_moverse.isActive():
            self.timer_moverse.stop()
    
    def enviar_movimiento(self):
        if self.active == True:
            self.x += self.velocidad
            self.parent.mover_proyectiles(self.numero_id, (self.x, self.y))

class Soles(QObject):
    def __init__(self, y, x, parent):
        super().__init__()
        self.parent = parent
        self.x = x
        self.y = y
        self.numero_id = ''
        self.aparicion = p.INTERVALO_SOLES_GIRASOL
#----------------------------------------------------------
class Plantas(QObject):
    senal_cambiar_foto = QTimer()
    def __init__(self,x, y, numero, parent):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.zombies_comiendosela = []
        self.numero_id = numero
        self._vida = p.VIDA_PLANTA
        self.dano = p.DANO_PROYECTIL
        self.realentizardor = False
        self.timer_disparo_pausado = False
        self.timer_disparo = QTimer()
        self.foto = 0
        self.parent = parent
        self.active = True
        self.configurar_timer()
    
    @property
    def vida(self):
        return self._vida 
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.eliminar()
        else:
            self._vida = valor

    def eliminar(self):
        self.parent.eliminar_planta(self.numero_id)
        self.active = False
        self.timer_disparo.stop()

    def configurar_timer(self):
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO//3)
        self.timer_disparo.timeout.connect(self.disparar_guisante)

    def disparar_guisante(self):
        if self.foto == 0:
            self.parent.planta_cambiar(self.numero_id, self.ruta0)
            self.foto += 1
        elif self.foto == 1:
            self.parent.planta_cambiar(self.numero_id, self.ruta1)
            self.foto += 1
            guiso = Proyectil(self.x, self.y, self.tipo, self.parent)
            self.parent.crear_proyectil_guisante(guiso)
            guiso.timer_moverse.start()
            
        elif self.foto == 2:
            self.parent.planta_cambiar(self.numero_id, self.ruta2)
            self.foto = 0

    def revisar_choque(self, pos):
        if self.y == pos[1]:
            if self.x + 70 >= pos[0] and \
                self.x + 40 <= pos[0]:
                return True
        return False
    
    def crear_proyectil(self, id):
        p = Proyectil(self.y, self.x, self.realentizar, id)
        self.proyectiles.append(p)
        return p

class PlantaClasica(Plantas):
    def __init__(self, x, y, numero, parent):
        super().__init__(x, y, numero, parent)
        self.tipo = 'lanzaguisantes'
        self.ruta0 = p.RUTA_GUISANTEB
        self.ruta1 = p.RUTA_GUISANTEC
        self.ruta2 = p.RUTA_GUISANTE
        self.costo = 100   

class PlantaAzul(Plantas):
    def __init__(self, x, y, numero, parent):
        super().__init__(x, y, numero, parent)
        self.tipo = 'lanzaguisantesHielo'
        self.ruta0 = p.RUTA_HIELOB
        self.ruta1 = p.RUTA_HIELOC
        self.ruta2 = p.RUTA_HIELO
        self.costo = 150
        self.realentizardor = True

class PlantaGirasol(QObject):
    def __init__(self, x, y, numero, parent):
        super().__init__()
        self.timer_disparo_pausado = False
        self.zombies_comiendosela = []
        self.x = x
        self.y = y
        self.numero_id = numero
        self.costo = 50
        self.tipo = 'girasol'
        self.vida = p.VIDA_PLANTA
        self.intervalo = p.INTERVALO_SOLES_GIRASOL
        self.cantidad = p.CANTIDAD_SOLES
        self.timer_disparo = QTimer()
        self.foto = 0
        self.parent = parent
        self.configurar_timer()
    
    @property
    def vida(self):
        return self._vida 
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.eliminar()
        else:
            self._vida = valor

    def eliminar(self):
        self.parent.eliminar_planta(self.numero_id)
        self.active = False
        self.timer_disparo.stop()    
    
    def configurar_timer(self):
        self.timer_disparo.setInterval(p.INTERVALO_SOLES_GIRASOL//2)
        self.timer_disparo.timeout.connect(self.crear_soles_a)
            
    def crear_soles_a(self):
        if self.foto == 0:
            self.parent.planta_cambiar(self.numero_id, p.RUTA_GIRASOLB)
            self.foto += 1  
                
        elif self.foto == 1:
            for _ in range(self.cantidad):
                sol = Soles(self.y - choice(p.POS_X_SOLES), self.x + choice(p.POS_X_SOLES), 
                            self.parent)
                self.parent.crear_soles(sol)
            self.parent.planta_cambiar(self.numero_id, p.RUTA_GIRASOL)
            self.foto = 0
    def revisar_choque(self, pos):
        if self.y == pos[1]:
            if self.x + 70 >= pos[0] and \
                self.x + 40 <= pos[0]:
                return True
        return False

class PlantaPatata(QObject):
    def __init__(self, x, y, numero, parent):
        super().__init__()
        self.zombies_comiendosela = []
        self.x = x
        self.y = y
        self.numero_id = numero
        self.costo = 75
        self.parent = parent
        self.tipo = 'patata'
        self._vida = 2*p.VIDA_PLANTA
        self.f1 = (2*p.VIDA_PLANTA*4)/5
        self.cambio1 = False
        self.f2 = p.VIDA_PLANTA
        self.cambio2 = False
    
    @property
    def vida(self):
        return self._vida 
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.eliminar()
        
        elif valor > self.f2 and valor <= self.f1:
            self._vida = valor
            if self.cambio1 == False:
                self.parent.planta_cambiar(self.numero_id, p.RUTA_PAPA2)
                self.cambio1 == True
       
        elif valor <= self.f2 and valor > 0:
            self._vida = valor
            if self.cambio2 == False:
                self.parent.planta_cambiar(self.numero_id, p.RUTA_PAPA3)
                self.cambio2 == True
        else:
            self._vida = valor
    
    def revisar_choque(self, pos):
        if self.y == pos[1]:
            if self.x + 70 >= pos[0] and \
                self.x + 40 <= pos[0]:
                return True
        return False

    def eliminar(self):
        self.parent.eliminar_planta(self.numero_id)
        self.active = False
#----------------------------------------------------------
class Zombies(QObject):
    def __init__(self, carril, x, y, parent):
        super().__init__()
        self.dano = p.DANO_MORDIDA
        self.intervalo = p.INTERVALO_TIEMPO_MORDIDA
        self._vida = 1
        self.carril = carril
        self._x = x
        self.y = y
        self.estado = 'caminando'
        self.velocidad = ''
        self.ruta = ''
        self.ruta_caminando = ''
        self.ruta_comiendo = ''
        self.ruta_comiendob = ''
        self.ruta_comiendoc = ''
        self.active = True
        self.realentizado = False
        self.numero_id = ''
        self.parent = parent
        self.foto = 0
        self.foto_comiendo = 0
        self.timer_comer_pausada = False
        self.timer_moverse_pausado = False
        self.llego_fin = False
        self.timer_moverse = QTimer()
        self.timer_comiendo = QTimer()
        self.configurar_timer()

    @property
    def vida(self):
        return self._vida 
    @vida.setter
    def vida(self, valor):
        if valor <= 0:
            self.eliminar()
        else:
            self._vida = valor
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, valor):
        if valor <= p.LIMITE_IZQUIERDA:
            self.llego_fin = True
        else:
            self._x = valor
    
    def configurar_timer(self):
        self.timer_moverse.setInterval(200)
        self.timer_moverse.timeout.connect(self.enviar_movimiento) 
        self.timer_comiendo.setInterval(p.INTERVALO_TIEMPO_MORDIDA//3)
        self.timer_comiendo.timeout.connect(self.enviar_comer)

    def enviar_comer(self):
        if self.active == True:
            if self.foto_comiendo == 0:
                self.parent.zombie_cambiar_foto(self.numero_id, 
                                                [self.x, self.y, self.ruta_comiendo])
                self.foto_comiendo += 1
            elif self.foto_comiendo == 1:
                self.parent.zombie_cambiar_foto(self.numero_id, 
                                                [self.x, self.y, self.ruta_comiendob])
                self.foto_comiendo += 1                
            elif self.foto_comiendo == 2:
                self.parent.zombie_comer(self.numero_id, 
                                        [self.x, self.y, self.ruta_comiendoc])
                self.foto_comiendo = 0 

    def enviar_movimiento(self):
        if self.active == True:
            if self.foto == 0:
                self.x -= self.velocidad
                self.parent.mover_zombies(self.numero_id, [self.x, self.y, self.ruta_caminando])    
                self.foto += 1
            elif self.foto == 1:
                self.parent.mover_zombies(self.numero_id, [self.x, self.y, self.ruta])
                self.foto -= 1

    def eliminar(self):
        self.parent.eliminar_zombie(self.numero_id, self.llego_fin)
        self.active = False
        self.timer_moverse.stop()

    def revisar_choque(self, pos):
        if pos[0] + 30 >= self.x and pos[0] <= self.x + 70 and \
                pos[1] == self.y:
            return True
        return False

class ZombieClasico(Zombies):
    def __init__(self, carril, x, y, parent):
        super().__init__(carril, x, y, parent)
        self.velocidad = p.VELOCIDAD_ZOMBIE
        self.ruta_caminando = p.RUTA_ZOMBIE_CLASICO
        self.ruta = p.RUTA_ZOMBIE_CLASICOB
        self.ruta_comiendo = p.RUTA_ZOMBIE_CLASICO_COMIENDO
        self.ruta_comiendob = p.RUTA_ZOMBIE_CLASICO_COMIENDOB
        self.ruta_comiendoc = p.RUTA_ZOMBIE_CLASICO_COMIENDOC

class ZombieRapido(Zombies):
    def __init__(self, carril, x, y, parent):
        super().__init__(carril, x, y, parent)
        self.velocidad = 1.5*p.VELOCIDAD_ZOMBIE
        self.ruta_caminando = p.RUTA_ZOMBIE_RUNNER
        self.ruta = p.RUTA_ZOMBIE_RUNNERB
        self.ruta_comiendo = p.RUTA_ZOMBIE_RUNNER_COMIENDO
        self.ruta_comiendob = p.RUTA_ZOMBIE_RUNNER_COMIENDOB
        self.ruta_comiendoc = p.RUTA_ZOMBIE_RUNNER_COMIENDOC
#----------------------------------------------------------