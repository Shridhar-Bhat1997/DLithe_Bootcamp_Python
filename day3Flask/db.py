
from flask import Flask, request, redirect, url_for, session, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = 'shri123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'shri'
app.config['MYSQL_PASSWORD'] = 'shri123'
app.config['MYSQL_DB'] = 'userprofile'

mysql = MySQL(app)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('Select * from users where username = %s and password =%s', (username, password))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            """message = 'login successful'"""
            return render_template('welcome.html', message=user)
        else:
            message = 'invalid credentials'
            return render_template('login.html', message=message)

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        postcode = request.form['postcode']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(
                """INSERT INTO users (username, password, email, phone, address, city, state, country, postcode)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (username, password, email, phone, address, city, state, country, postcode))

            mysql.connection.commit()
            return redirect(url_for('login'))
        except MySQLdb.IntegrityError as e:

            return f"{e}"

    return render_template('registration.html')

@app.route('/updateuser/<int:id>', methods=['GET','POST'])
def updateuser(id):
    message = ''
    if request.method=='GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from users where id=%s',(id,))
        data = cursor.fetchone()
        if data!=None:
            return render_template('updateuser.html', message=data)

        return redirect(url_for('register'))
    if request.method == 'POST':
        ID=id
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        postcode = request.form['postcode']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            """ UPDATE users
            SET username=%s,password=%s,email=%s,phone=%s,address=%s,city=%s,
             state=%s,country=%s,postcode=%s where id=%s""",(username,password,email,phone,address,city,state,country,postcode,ID)
            )

        mysql.connection.commit()
        cursor.execute('select * from users where id=%s', (id,))
        data = cursor.fetchone()
        return render_template('welcome.html',message=data)




@app.route('/deleteuser/<int:id>',methods=['GET'])
def deleteduser(id):
    if request.method=='GET':
        identity=id
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from users where id=%s ', (id,))
        data = cursor.fetchone()
        if data!=None:
            cursor.execute('delete from users where id=%s and id=%s',(identity,identity))
            mysql.connection.commit()
            return redirect(url_for('home'))
        return f'User with id {id} do not exist'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='83', debug=True)