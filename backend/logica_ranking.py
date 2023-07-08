from PyQt5.QtCore import QObject, pyqtSignal

class LogicaRanking(QObject):

    senal_respuesta_ordenado = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.nombre = ''
    
    def cargar_ranking(self):

        def ordenar_ranking(sublista):
            return sublista[1]

        with open('puntajes.txt') as file:
            lista = file.readlines()
            for i in range(len(lista)):
                lista[i] = lista[i].strip().split(',')
                lista[i][1] = int(lista[i][1])

        lista.sort(key = ordenar_ranking, reverse = True)
        self.senal_respuesta_ordenado.emit(lista[0:5])

    def cargar_datos(self, puntaje):
        with open('puntajes.txt', 'r') as file:
            lista = file.readlines()
            for i in range(len(lista)):
                lista[i] = lista[i].strip().split(',')
                lista[i][1] = int(lista[i][1])
            verificador = False
            for i in range(len(lista)):
                if lista[i][0] == self.nombre:
                    lista[i][1] += puntaje
                    verificador = True
            if verificador == False:
                lista.append([self.nombre, puntaje])
            nueva = []
            for i in range(len(lista)):
                lista[i][1] = str(lista[i][1]) + '\n'
                x = ','.join(lista[i])
                nueva.append(x)
            with open('puntajes.txt', 'w') as puntajes_actualizados:
                for usuario in nueva:
                    puntajes_actualizados.write(usuario)

    def cargar_nombre(self, nombre):
        self.nombre = nombre