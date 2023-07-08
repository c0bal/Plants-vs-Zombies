from PyQt5.QtWidgets import QApplication
from backend.logica_inicio import LogicaInicio
from backend.logica_ranking import LogicaRanking
from backend.logica_juego import LogicaJuego
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post import VentanaPost
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ranking import VentanaRanking

class DCCruz(QApplication):
    def __init__(self, arg):
        super().__init__(arg)
    
        # Instanciar Ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_ranking = VentanaRanking()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_post = VentanaPost()

        #Instanciar Logicas 
        self.logica_inicio = LogicaInicio()
        self.logica_ranking = LogicaRanking()
        self.logica_juego = LogicaJuego()

        self.conectar_inicio()
        self.conectar_ranking()
        self.conectar_principal()
        self.conectar_juego()
        self.conectar_pos()
        
    def conectar_inicio(self):

        self.ventana_inicio.senal_enviar_login.connect(
            self.logica_inicio.comprobar_usuario)
        self.logica_inicio.senal_respuesta_validacion.connect(
            self.ventana_inicio.recibir_validacion)
        self.logica_inicio.senal_abrir_juego.connect(
            self.ventana_principal.mostrar_ventana)
        self.ventana_inicio.senal_enviar_ranking.connect(
            self.logica_ranking.cargar_ranking)
        self.ventana_inicio.senal_enviar_usuario.connect(
            self.logica_ranking.cargar_nombre)
    
    def conectar_ranking(self):
        
        self.logica_ranking.senal_respuesta_ordenado.connect(
            self.ventana_ranking.abrir)
        self.ventana_ranking.senal_volver_inicio.connect(
            self.iniciar)
    
    def conectar_principal(self):
        self.ventana_principal.senal_ingresar_juego.connect(
            self.logica_juego.apertura)
        
        self.logica_juego.senal_cargar_datos_iniciales.connect(
            self.ventana_juego.abrir)
    
    def conectar_juego(self):
        self.ventana_juego.senal_avanzar_ronda.connect(
            self.logica_juego.avanzar)

        self.logica_juego.senal_esconder_objetos_fin.connect(
            self.ventana_juego.esconder_objetos)
        
        self.logica_juego.senal_salvado_zombies.connect(
            self.ventana_juego.mostrar_salvado)
        self.logica_juego.senal_actualizar_juego.connect(
            self.ventana_juego.setear_datos)

        self.ventana_juego.senal_iniciar_juego.connect(
            self.logica_juego.iniciar)
        self.ventana_juego.senal_plantar.connect(
            self.logica_juego.poner_planta)
        
        self.logica_juego.senal_crear_proyectil.connect(
            self.ventana_juego.crear_proyectil)
        self.ventana_juego.senal_disparos_creados.connect(
            self.logica_juego.eliminiar_disparos_creados)

        self.logica_juego.senal_mover_proyectiles.connect(
            self.ventana_juego.mover_proyectiles)
        self.ventana_juego.senal_proyectiles_movidos.connect(
            self.logica_juego.eliminar_proyectiles_movidos)

        self.logica_juego.senal_cambiar_foto_plantas.connect(
            self.ventana_juego.cambiar_imagen_plantas)
        self.ventana_juego.senal_plantas_cambiadas.connect(
            self.logica_juego.eliminar_plantas_cambiados)
        self.logica_juego.senal_eliminar_planta.connect(
            self.ventana_juego.eliminar_planta)
        self.ventana_juego.senal_mate_planta.connect(
            self.logica_juego.eliminar_plantas_eliminadas)

        self.logica_juego.senal_eliminar_proyectil.connect(
            self.ventana_juego.eliminar_proyectiles)
        self.ventana_juego.senal_proyectiles_eliminados.connect(
            self.logica_juego.eliminar_proyectiles_eliminados)
        self.logica_juego.senal_cambiar_proyectil.connect(
            self.ventana_juego.cambiar_proyectil)
        self.ventana_juego.senal_cambie_proyectil.connect(
            self.logica_juego.eliminar_proyectiles_a_cambiar)

        self.logica_juego.senal_crear_zombie.connect(
            self.ventana_juego.crear_zombie)
        self.logica_juego.senal_cambiar_foto_zombie.connect(
            self.ventana_juego.cambiar_imagen_zombie)
        self.ventana_juego.senal_movi_zombies.connect(
            self.logica_juego.eliminar_zombies_movidos)
        self.logica_juego.senal_eliminar_zombie.connect(
            self.ventana_juego.eliminar_zombies)
        self.ventana_juego.senal_mate_zombies.connect(
            self.logica_juego.eliminar_zombies_eliminados)
        
        self.logica_juego.senal_crear_soles.connect(
            self.ventana_juego.crear_sol)
        self.ventana_juego.senal_soles_creados.connect(
            self.logica_juego.eliminar_soles_creados)
        self.ventana_juego.senal_agarrar_sol.connect(
            self.logica_juego.agarrar_sol)

        self.logica_juego.senal_terminar_ronda.connect(
            self.ventana_post.abrir)
        self.logica_juego.senal_cerrar_ventana_juego.connect(
            self.ventana_juego.cerrar)
        self.logica_juego.senal_reset_ventana_juego.connect(
            self.ventana_juego.reset)
        self.ventana_juego.senal_pausar_juego.connect(
            self.logica_juego.pausar)
        self.ventana_juego.senal_reanudar_juego.connect(
            self.logica_juego.reanudar)

        self.logica_juego.senal_siguiente_ronda.connect(
            self.ventana_juego.siguiente_ronda)

        self.logica_juego.senal_te_mataron.connect(
            self.ventana_juego.te_mataron)

        self.ventana_juego.senal_cheat_kill.connect(
            self.logica_juego.kill_all)
        self.ventana_juego.senal_cheat_sun.connect(
            self.logica_juego.soles_extra)

        self.ventana_juego.senal_salir.connect(
            self.logica_juego.salir_ronda)

    def conectar_pos(self):
        
        self.ventana_post.senal_siguiente_ronda.connect(
            self.logica_juego.siguiente_ronda)
        self.ventana_post.senal_cargar_datos.connect(
            self.logica_ranking.cargar_datos)
        self.ventana_post.senal_abrir_inicio.connect(
            self.iniciar)

    def iniciar(self):
        self.ventana_inicio.show()
