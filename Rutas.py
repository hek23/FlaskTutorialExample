# -*- coding: cp1252 -*-

from flask import Flask
from math import sqrt

app = Flask(__name__)

#Se define una clase que representa a los puntos
class Punto :
    def __init__(self, coordenadas, adyacentes) :
        #Coordenadas del punto en latitud y longitud
        self.coordenadas = coordenadas
        #Puntos adyacentes (momentamneamente representados como número para la prueba)
        self.adyacentes = adyacentes

#Función que rellena con 10 la base de la matriz de adyacencias, recibiendo
#la cantidad de puntos como entrada
        
def rellenarMatriz(nPuntos) :
    adyacencias = []
    i = 0
    while i < nPuntos :
        adyacencias.append([])
        j = 0
        while j < nPuntos :
            adyacencias[i].append(10)
            j += 1
        i += 1
    return adyacencias

#Función que dados dos puntos, calcula su distancia entre ellos mediante
#propiedades geométricas

def calcularDistancia(punto1, punto2) :
    x = punto1[0] - punto2[0]
    y = punto1[1] - punto2[1]
    return sqrt(x**2 + y**2)

#Función que completa la matriz de adyaciencias, recibiendo la base de esta (una matriz
#de -1) y una lista de objetos Punto

def completarAdyacencias(adyacencias, puntos) :
    i = 0
    while i < len(adyacencias) :
        #Establezco que la distancia es nula entre el punto y si mismo
        adyacencias[i][i] = 0
        #Reconozco las adyacencias que tiene el punto
        for adyacente in puntos[i].adyacentes :
            #Asigno la distancia entre el punto y sus adyacentes en la matriz de adyacencias
            adyacencias[i][adyacente] = calcularDistancia(puntos[i].coordenadas, puntos[adyacente].coordenadas)
            #print adyacente
            #print puntos[adyacente].coordenadas
            #print puntos[i].coordenadas
            #print adyacencias[i][adyacente]
        i += 1
    return adyacencias
        



#Función que implementa el algoritmo Dijsktra para encontrar el camino mínimo
#dado un punto de origen y una matriz de adyacencias
def dijkstra(origen, adyacencias) :
    #Matriz donde la primera fila corresponde a la distancia desde el punto
    #de origen al punto dado y la segundo corresponde al punto predecesor
    caminos = [[],[]]
    i = 0
    for distancia in adyacencias[origen] :
        caminos[0].append(adyacencias[origen][i])
        caminos[1].append(origen)
        i += 1
    puntos = caminos[0][0:]
    puntos[origen] = 100
    i = 0
    while i < len(adyacencias)-1:
        minimo = min(puntos)
        posMin = puntos.index(minimo)
        puntos[posMin] = 100
        j = 0
        while j < len(adyacencias) :
            ####Buscar el mínimo de los que no se han revisado
            if caminos[0][posMin] + adyacencias[posMin][j] < caminos[0][j]:
                caminos[0][j] = caminos[0][posMin] + adyacencias[posMin][j]
                puntos[j] = caminos[0][posMin] + adyacencias[posMin][j]
                caminos[1][j] = posMin
            j += 1
        i += 1
    return caminos

#Función que determina el camino más cortos hasta un punto, de acuerdo al punto de
#origen establecido en dijkstra y los puntos que pasan por este camino

def encontrarCamino(dijkstra, destino) :
    #datos incluye en su primera posición la distancia mínima y en su segunda los puntos del camino
    datos = [0,[destino]]
    punto = destino
    llegada = False
    while True:
        #Se pregunta si el punto antecesor es el origen
        if dijkstra[1][punto] == 0 :
            datos[1].append(0)
            datos[0] += dijkstra[0][punto]
            return datos
        #Si no lo es, continúa el ciclo buscando el origen
        else:
            datos[0] += dijkstra[0][punto]
            datos[1].append(dijkstra[1][punto])
            punto = dijkstra[1][punto]

#Función que retorna una lista con los puntos del camino más corto desde un punto a otro

def encontrarPuntos(camino, puntos) :
    puntosCamino = []
    for punto in camino :
        puntosCamino.append({"lat": puntos[punto].coordenadas[0] , "lng": puntos[punto].coordenadas[1]})
    return puntosCamino
##prueba = dijkstra(0, adyacencias)

#print prueba

puntos = []

puntos.append(Punto([-33.449385, -70.682128], [1,2]))
puntos.append(Punto([-33.449019, -70.683184], [0,3]))
puntos.append(Punto([-33.448459, -70.682078], [0,6,7,11]))
puntos.append(Punto([-33.448395, -70.683129], [1,4]))
puntos.append(Punto([-33.448418, -70.682655], [3,5,8]))
puntos.append(Punto([-33.448434, -70.682408], [4,6,9])) #5
puntos.append(Punto([-33.448445, -70.682231], [2,5,10]))  #6
puntos.append(Punto([-33.448463, -70.681885], [2,12]))
puntos.append(Punto([-33.447758, -70.682599], [4,9]))
puntos.append(Punto([-33.447772, -70.682354], [5,8,10]))
puntos.append(Punto([-33.447787, -70.682186], [6,9,11]))
puntos.append(Punto([-33.447790, -70.682011], [2,10,12]))
puntos.append(Punto([-33.447800, -70.681833], [7,11]))

adyacencias = rellenarMatriz(len(puntos))

adyacencias = completarAdyacencias(adyacencias, puntos)

@app.route('/')
@app.route('/<int:origen>/')
@app.route('/<int:origen>/<int:destino>/')
def encontrarRuta(origen = 0, destino = 2) :
	rutas = dijkstra(origen, adyacencias)
	camino = encontrarCamino(rutas, destino)
	ruta = encontrarPuntos(camino[1], puntos)
	return str(ruta)

app.run(debug = True)
