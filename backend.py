# backend.py

import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS BOOK (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def issue():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS issue (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def request():
    conn = sqlite3.connect("request.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS request (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO BOOK VALUES(NULL,?,?,?,?)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def request_insert(title, author, year, isbn):
    conn = sqlite3.connect('request.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO request VALUES(NULL,?,?,?,?)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def request_view(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('request.db')
    cur = conn.cursor()
    query = "SELECT * FROM request WHERE title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?"
    cur.execute(query, ('%'+title+'%', '%'+author+'%', '%'+year+'%', '%'+isbn+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def request_delete(title):
    conn = sqlite3.connect('request.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM request WHERE title=?", (title,))
    conn.commit()
    conn.close()

def issue_delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM issue WHERE id=?", (id,))
    conn.commit()
    conn.close()

def issue_insert(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO issue SELECT * FROM BOOK WHERE id=?', (id,))
    conn.commit()
    conn.close()

def issue_view(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    query = "SELECT * FROM issue WHERE title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?"
    cur.execute(query, ('%'+title+'%', '%'+author+'%', '%'+year+'%', '%'+isbn+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM BOOK")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    query = "SELECT * FROM BOOK WHERE title LIKE ? AND author LIKE ? AND year LIKE ? AND isbn LIKE ?"
    cur.execute(query, ('%'+title+'%', '%'+author+'%', '%'+year+'%', '%'+isbn+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM BOOK WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE BOOK SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
