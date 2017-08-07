#Archivo de configuracion

import os

#Creamos una clase que tiene las configuraciones generales
#Hereda de object, para que sea instanciable
class Config(object):
    #Aquí como son constantes, son con palabras en mayuscula
    PORT = 5000
    
#Ahora, podemos crear clases hijo para los diferentes entornos

class DevelopmentConfig(Config):
    PORT = 9000
    DEBUG = True



