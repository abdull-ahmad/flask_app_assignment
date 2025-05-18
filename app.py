"""
A simple Flask web application providing user authentication.
This app enables user registration, login, and session management.
"""
import sqlite3

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_key'

def init_db():
    """Initialize the SQLite database with users table if it doesn't exist."""
    with sqlite3.connect('users.db') as con:
        con.execute(
            'CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)'
        )

@app.route('/')
def index():
    """Render the home page if user is logged in, otherwise redirect to login."""
    if 'user' in session:
        with sqlite3.connect('users.db') as con:
            cur = con.cursor()
            users = cur.execute("SELECT username FROM users").fetchall()
        return render_template('home.html', users=users)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login requests and authenticate credentials."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('users.db') as con:
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM users WHERE username=? AND password=?", 
                (username, password)
            )
            user = cur.fetchone()
            if user:
                session['user'] = username
                return redirect('/')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration requests and store new user information."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('users.db') as con:
            try:
                con.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)", 
                    (username, password)
                )
                con.commit()
                return redirect('/login')
            except sqlite3.IntegrityError:
                return "Username already exists"
    return render_template('register.html')

@app.route('/logout')
def logout():
    """Remove the user from session and redirect to login page."""
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
