from os import path
# Los intervalos están en milisegundos
INTERVALO_DISPARO = 2000 
INTERVALO_SOLES_GIRASOL = 2000
INTERVALO_TIEMPO_MORDIDA = 5000
# El daño y la vida tienen las mismas medidas
DANO_PROYECTIL = 5
DANO_MORDIDA = 5
VIDA_PLANTA = 100
VIDA_ZOMBIE = 80
# Número de zombies por carril
N_ZOMBIES = 7
# Porcentaje de ralentización
RALENTIZAR_ZOMBIE = 0.25
# Soles iniciales por ronda
SOLES_INICIALES = 250
# Número de soles generados por planta
CANTIDAD_SOLES = 2
POS_X_SOLES = [10, 20, 30, 40, 50, 60]
ACTUALIZAR_JUEGO = 2

# Número de soles agregados a la cuenta por recolección
SOLES_POR_RECOLECCION = 50
# Número de soles agregados a la cuenta por Cheatcode
SOLES_EXTRA = 25
# Ponderadores de escenarios
PONDERADOR_NOCTURNO = 0.8
PONDERADOR_DIURNO = 0.9
# La velocidad del zombie en milisegundos
VELOCIDAD_ZOMBIE = 5
# Puntaje por eliminar zombie
PUNTAJE_ZOMBIE_DIURNO = 50
PUNTAJE_ZOMBIE_NOCTURNO = 100
# Costo por avanzar de ronda
COSTO_AVANZAR = 500
# Costo tiendas
COSTO_LANZAGUISANTE = 50
COSTO_LANZAGUISANTE_HIELO = 100
COSTO_GIRASOL = 50
COSTO_PAPA = 75
# Caracteres de nombre usuario
MIN_CARACTERES = 3
MAX_CARACTERES = 15


ACTUALIZAR_DISPAROS = 40
ACTUALIZAR_CAMINATA = 250
VELOCIDAD_GUISO = 10

LIMITE_DERECHA = 1241
LIMITE_IZQUIERDA = 330

# Rutas 
RUTA_UI_INICIO = path.join('frontend', 'assets', 'ui_files', 'ventana_inicio.ui')
RUTA_UI_RANKING = path.join('frontend', 'assets', 'ui_files', 'ventana_ranking.ui')
RUTA_UI_PRINCIPAL = path.join('frontend', 'assets', 'ui_files', 'ventana_principal.ui')
RUTA_UI_JUEGO = path.join('frontend', 'assets', 'ui_files', 'ventana_juego.ui')
RUTA_UI_POST = path.join('frontend', 'assets', 'ui_files', 'ventana_post_ronda.ui')

RUTA_CRAZY = path.join('frontend', 'assets', 'sprites', 'CrazyRuz', 'crazyCruz.png')
RUTA_MUERTE = path.join('frontend', 'assets', 'sprites', 'Elementos de juego', 'textoFinal.png')


RUTA_GUISANTE = path.join('frontend', 'assets', 'sprites','Plantas', 'lanzaguisantes_1.png')
RUTA_GUISANTEB = path.join('frontend', 'assets', 'sprites','Plantas', 'lanzaguisantes_2.png')
RUTA_GUISANTEC = path.join('frontend', 'assets', 'sprites','Plantas', 'lanzaguisantes_3.png')

RUTA_GIRASOL = path.join('frontend', 'assets', 'sprites', 'Plantas', 'girasol_1.png')
RUTA_GIRASOLB = path.join('frontend', 'assets', 'sprites', 'Plantas', 'girasol_2.png')

RUTA_SOL = path.join('frontend', 'assets', 'sprites', 'Elementos de juego', 'sol.png')

RUTA_HIELO = path.join('frontend', 'assets', 'sprites', 'Plantas', 'lanzaguisantesHielo_1.png')
RUTA_HIELOB = path.join('frontend', 'assets', 'sprites', 'Plantas', 'lanzaguisantesHielo_2.png')
RUTA_HIELOC = path.join('frontend', 'assets', 'sprites', 'Plantas', 'lanzaguisantesHielo_3.png')

RUTA_PAPA = path.join('frontend', 'assets', 'sprites', 'Plantas', 'papa_1.png')
RUTA_PAPA2 = path.join('frontend', 'assets', 'sprites', 'Plantas', 'papa_2.png')
RUTA_PAPA3 = path.join('frontend', 'assets', 'sprites', 'Plantas', 'papa_3.png')

RUTA_FONDO_NOCHE = path.join('frontend', 'assets', 'sprites', 'Fondos', 'salidaNocturna.png')
RUTA_FONDO_DIA = path.join('frontend', 'assets', 'sprites', 'Fondos', 'jardinAbuela.png')

RUTA_PROYECTIL_VERDE = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisante_1.png')
RUTA_PROYECTIL_VERDEB = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisante_2.png')
RUTA_PROYECTIL_VERDEC = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisante_3.png')

RUTA_PROYECTIL_AZUL = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisanteHielo_1.png')
RUTA_PROYECTIL_AZULB = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisanteHielo_2.png')
RUTA_PROYECTIL_AZULC = path.join('frontend', 'assets', 'sprites','Elementos de juego', 'guisanteHielo_3.png')

RUTA_ZOMBIE_CLASICO = path.join('frontend', 'assets', 'sprites','Zombies', 'Caminando', 'zombieNicoWalker_1.png')
RUTA_ZOMBIE_CLASICOB = path.join('frontend', 'assets', 'sprites','Zombies', 'Caminando', 'zombieNicoWalker_2.png')
RUTA_ZOMBIE_RUNNER = path.join('frontend', 'assets', 'sprites','Zombies', 'Caminando','zombieHernanRunner_1.png')
RUTA_ZOMBIE_RUNNERB = path.join('frontend', 'assets', 'sprites','Zombies', 'Caminando','zombieHernanRunner_2.png')

RUTA_ZOMBIE_CLASICO_COMIENDO = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieNicoComiendo_1.png')
RUTA_ZOMBIE_CLASICO_COMIENDOB = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieNicoComiendo_2.png')
RUTA_ZOMBIE_CLASICO_COMIENDOC = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieNicoComiendo_3.png')
RUTA_ZOMBIE_RUNNER_COMIENDO = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieHernanComiendo_1.png')
RUTA_ZOMBIE_RUNNER_COMIENDOB = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieHernanComiendo_2.png')
RUTA_ZOMBIE_RUNNER_COMIENDOC = path.join('frontend', 'assets', 'sprites','Zombies', 'Comiendo', 'zombieHernanComiendo_3.png')