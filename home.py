from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
def get_userdb_connection():
    users_db = sqlite3.connect('library_users.db')
    user_cursor = users_db.cursor()
    users_db.commit()
    return users_db




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name=request.form['username']
        password=request.form['password']
        return render_template('admin.html',name=name,password=password)

app.run(debug=True)