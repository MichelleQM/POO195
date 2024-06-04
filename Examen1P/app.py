from flask import Flask, request, render_template

app = Flask(__name__)

#RUTA DE HOME
@app.route('/')
def Home():
    return 'HOME'

@app.route('/formulario')
def Formulario():
    return render_template('/index.html')

#RUTA PARA NUMERO AL CUADRADO 
@app.route('/numeroalcuadrado/<int:num>', methods=['GET'])
def numeroalcuadrado(num):
    return str(num ** 2)

#PARA RUTA DE ERROR
@app.errorhandler(404)
def paginano(e):
    return 'No se encontro la pagina deseada: Revisa tu sintaxis'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    