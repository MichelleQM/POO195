from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
app.config['MYSQL_DB'] = 'dbflask'

app.secret_key = 'millavesecreta'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarAlbum', methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        # Tomamos los datos que vienen por POST
        FTitulo = request.form['txtTitulo']
        FArtista = request.form['txtArtista']
        FAnio = request.form['txtAnio']
        
        # Enviamos a la BD
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO albums(titulo, artista, anio) VALUES (%s, %s, %s)', (FTitulo, FArtista, FAnio))
        mysql.connection.commit()
        
        flash('Album Guardado correctamente')
        return redirect(url_for('index'))

@app.errorhandler(404)
def paginanotfound(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=3000, debug=True)




