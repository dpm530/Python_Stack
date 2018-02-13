from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key='secret'
mysql = MySQLConnector(app,'login')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
@app.route('/')

def index():

    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create():

    query = "INSERT INTO users (first_name,last_name,username,password,confirm_password,created_at, updated_at) VALUES (:first_name, :last_name,:username,password,confirm_password,NOW(), NOW())"

    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'username': request.form['username'],
             'password': request.form['password'],
             'confirm_password': request.form['confirm_password']
           }

    if len(data['first_name'])<1 or len(data['last_name'])<1 or len(data['username'])<1 or len(data['password'])<8 or data['passowrd'] != data['confirm_password']:
        print "Wassuuuuuuuuuuuup!!!!///// Error!! Error!! Error!!, Try again :)"

    if not EMAIL_REGEX.match(data['username']):
        print "Invalid Character"

    value=mysql.query_db(query, data)

    return render_template('success.html')

@app.route('/login_a', methods=[POST])

def login():

    query= 'SELECT users.username,users.password FROM users'
    data = {
             'username': request.form['username'],
             'password': request.form['password'],
           }

   user=mysql.query_db(query, data)[0]

    if data['username']==user.username and data[password]==user.password:
        print "True"



    return render_template('success.html')

app.run(debug=True)
