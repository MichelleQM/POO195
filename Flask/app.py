from flask import Flask, request

app = Flask(__name__)

#RUTA SIMPLE
@app.route('/')
def principal():
    return 'Hola Mundo Flask'

#RUTA DOBLE 
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return 'Hola Michelle Quintero'

#RUTA CON PARAMENTROS 
@app.route('/hi/<nombre>')
def hi(nombre):
    return 'Hola' + nombre + '!!!'

#DEFINICION DE LOS METODOS DE TRABAJO 
@app.route('/formulario', methods = ['GET','POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar password por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para password'

#Manejo de excepciones para rutas 
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: No encontre nada'

if __name__ == '__main__':
    app.run(port=3000,debug=True)