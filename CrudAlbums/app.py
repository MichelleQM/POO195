from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] ="localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
app.config['MYSQL_DB'] = 'dbflask'

app.secret_key = 'millavesecreta'
mysql = MySQL(app)

@app.route('/')
def index():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM albums')
        consultaA = cursor.fetchall()
        #print(consultaA)
        return render_template('index.html', albums= consultaA)
    except Exception as e:
        print(e)
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
    
@app.route('/edita/<id>r')
def editar(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM albums WHERE idAlbum = %s', (id))
    albumE = cur.fetchone()
    return render_template('editar.html', albumE = albumE)

@app.errorhandler(404)
def paginanotfound(e):
    return 'Revisa tu sintaxis: No encontré nada'

if __name__ == '__main__':
    app.run(port=5000, debug=True)




