from flask import Flask, request, redirect,url_for, session, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app=Flask(__name__)

app.secret_key = 'shri1234'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='shri'
app.config['MYSQL_PASSWORD']='shri123'
app.config['MYSQL_DB']='userprofile'

mysql=MySQL(app)

@app.route('/login',methods=['GET','POST'])
def login():
    message=''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password=request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('Select * from user where username = %s and password =%s',(username,password))
        user=cursor.fetchone()
        if user:
            session['loggedin']=True
            session['id']=user['id']
            session['username']=user['username']
            message='login successful'
            return render_template('home.html',message=message)
        else:
            message='invalid credentials'
            return render_template('login.html',message=message)

    
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        phone=request.form['phone']
        address=request.form['address']
        city=request.form['city']
        state=request.form['state']
        country=request.form['country']
        postcode=request.form['postcode']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('insert into user (username,password,email,phone,address,city,state,country,postcode) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(username,password,email,phone,address,city,state,country,postcode))
        mysql.connection.commit()
        
        return redirect('/login')

    return render_template('register.html')


if __name__=="__main__":
    app.run(host='0.0.0.0',port='85',debug=True)