from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

mysql = MySQL(app) #generamos un objeto que nos permita acceder 
#a todas las funciones de la base de datos. 

#RUTA SIMPLE
@app.route('/pruebaConexion/')
def pruebaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        datos = cursor.fetchone()
        return jsonify({'status': 'conexion exitosa', 'data': datos})
    except Exception as ex:
        return jsonify({'status': 'Error de conexion', 'mensaje': str(ex)})


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
    app.run(port=6000,debug=True)
    