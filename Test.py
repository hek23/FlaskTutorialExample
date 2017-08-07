from flask import Flask
from flask import request

#Estatico, no cambiar
app = Flask(__name__)

#Decorador. Indica una referencia o ruta a la funcion indicada abajo
@app.route('/')
def index():
    return "wololo"
#Uso de parámetros. Especialmente util para peticiones Get
#Ej: http://localhost:5000/paramEj?argum1=ArgumentoEjemplo&argum2=PeticionGet
#Para extraer los valores de los parametros, se utiliza la expresion
#request.args.get(). Request contiene todos los datos de la consulta a la API
#tales como el paquete de parámetros, verbo HTTP y varias otras cosas que no se explicaran
#Así, en el ejemplo el primer argumento de request.args.get es el nombre del parametro
#en la peticion HTTP y el segundo el valor que obtiene el parametro si no se encuentra en la peticion

#En el return se utiliza format, que simplemente reemplaza las llaves por los parametros de la funcion format en orden
@app.route('/paramEj')
def ejemploParametros():   
    parametro1 = request.args.get('argum1', "fail!")
    parametro2 = request.args.get('argum2', "fail!")
    parametro3 = request.args.get('parametro', "valor por defecto")
    return "El parametro 1 es {}, el parametro 2 es {} y el parametro 3 es {}".format(parametro1, parametro2, parametro3)

#Rutas con validacion, tambien usado para metodo GET
#Existen circunstancias donde se quiere tener diversos comportamientos según los valores de entrada
#e incluso utilizar otro tipo de rutas como la mostrada en la funcion que sigue
#Dentro de ella, lo escrito entre signos menor mayor (< >), es el parámetro que PUEDE
#existir, pero también puede que no, por ello se debe marcar el valor por defecto. Además se referencia a una sola función
#desde dos rutas distintas

@app.route('/multiparam/')
@app.route('/multiparam/<argumentoOpc>/')
def multiparam(valor = 'valorpordefecto'):
    return valor
if __name__ == "__main__":
#Inicia la instancia de Flask
#Opciones:
#port: puerto para el servidor rest. Por default es 5000
#debug: activa modo debug (booleano). Activar para desarrollar
    app.run(debug = True)