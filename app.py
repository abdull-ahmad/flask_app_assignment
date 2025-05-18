from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

def init_db():
    with sqlite3.connect('users.db') as con:
        con.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)')

@app.route('/')
def index():
    if 'user' in session:
        with sqlite3.connect('users.db') as con:
            cur = con.cursor()
            users = cur.execute("SELECT username FROM users").fetchall()
        return render_template('home.html', users=users)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('users.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            user = cur.fetchone()
            if user:
                session['user'] = username
                return redirect('/')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('users.db') as con:
            try:
                con.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                con.commit()
                return redirect('/login')
            except:
                return "Username already exists"
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')