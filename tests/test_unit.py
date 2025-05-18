import sqlite3

def test_user_table():
    with sqlite3.connect('users.db') as con:
        result = con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'").fetchone()
        assert result is not None