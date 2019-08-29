from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import bcrypt

#la SAL, necesaria para la encriptación
sal = bcrypt.gensalt()

#configuración del servidor
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'usu'

mysql = MySQL(app)

#session Key
app.secret_key = "esta es mi clave secreta y es muy puto el que lo lea"

#Función Login
@app.route('/login', methods = ['POST'])
def Login():
        if request.method == 'POST':
                correo = request.form['correo']
                password = request.form['password']
                cur = mysql.connection.cursor()
                cur.execute('SELECT * FROM usuarios WHERE correo = %s', [correo])
                usu = cur.fetchone()
                if bcrypt.checkpw(password.encode('utf8'),usu[3].encode('utf8')):
                        session['name'] = correo
                        flash('Bienvenid@ ' + str(usu[1]))                        
                        return redirect(url_for('Index'))
                else:
                         flash('Datos erroneos')
                         return redirect(url_for('Index'))


#Función logout
@app.route('/logout')
def Logout():
        session.clear()
        return redirect(url_for('Index'))

#Función index
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    date = cur.fetchall()
    return render_template('index.html', usuarios = date)

#Función Update
@app.route('/update/<string:id>')
def Update(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE id = %s',[id])
        datos = cur.fetchall()
        return render_template('update.html', usuario = datos[0])

#Editar datos de usuario
@app.route('/update_usu/<string:id>', methods = ["POST"])
def Up_usu(id):
        if request.method == 'POST':
                name = request.form['nombre']
                correo = request.form['correo']
                password_prepare = request.form['password'].encode()
                password = bcrypt.hashpw(password_prepare, sal)
                cur = mysql.connection.cursor()
                cur.execute('''UPDATE usuarios 
                                SET datos = %s,
                                correo = %s, 
                                password = %s 
                                WHERE id = %s''',(name,correo,password,id))
                mysql.connection.commit()
                flash('contacto modificado')
                return redirect(url_for('Index'))

#Función de registro
@app.route('/signin', methods=['POST'])
def SignIn():
    if request.method == 'POST':
        name = request.form['nombre']
        correo = request.form['correo']
        password_prepare = request.form['password'].encode()
        password = bcrypt.hashpw(password_prepare, sal)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (datos, correo, password) VALUES (%s,%s,%s)',
        [name, correo, password])
        mysql.connection.commit()
        flash('contacto agregado satisfactoriamente')

        return redirect(url_for('Index'))

#función de borrado
@app.route('/delete/<string:id>')
def Delete(id):
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM usuarios WHERE id = %s',[id])
        mysql.connection.commit()
        flash('contacto eliminado')
        return redirect(url_for('Index'))

#Arranque del servidor
if __name__ == '__main__':
    app.run(port = 3000, debug = True)