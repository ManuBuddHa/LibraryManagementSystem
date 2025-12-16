from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import psycopg2
c=psycopg2.connect(user="postgres",password="admin",port=5432,host="localhost",database="users")
c.autocommit=True
conn=c.cursor()
# conn.execute("create database users")
app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def sample():
    return render_template('admin.html')

@app.route('/viewmembers')
def viewmembers():
    return render_template('viewmembers.html')

@app.route('/addmembers')
def addmembers():
    return render_template('addmembers.html')

@app.route('/viewbooks')
def viewbooks():
    return render_template('viewbooks.html')

@app.route('/addbooks')
def addbooks():
    return render_template('addbooks.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        mobile = request.form['mobile']


app.run(debug=True)