import sqlite3
from tkinter import *
from tkinter import messagebox  # Importing messagebox for showing errors

from admin import admin  # Assuming admin and student are defined in admin.py and student.py
from student import student


def connect():
    conn = sqlite3.connect("login.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user(roll_no INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS admin(roll_no INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    conn.commit()
    conn.close()


def insert(rollno, name, password):
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO user VALUES(?,?,?)', (rollno, name, password))
    conn.commit()
    conn.close()


def check(name, password):
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM admin WHERE name = ? AND password = ?', (name, password))
    if cur.fetchone():
        conn.close()
        window = Tk()
        window.title('Admin_User')
        window.geometry('700x450')
        obj = admin(window)
        window.mainloop()
    else:
        conn.close()
        messagebox.showinfo('error', 'INVALID CREDENTIALS for ADMIN LOGIN')


def checks(name, password):
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM user WHERE name = ? AND password = ?', (name, password))
    if cur.fetchone():
        conn.close()
        window = Tk()
        window.title('Student_User')
        window.geometry('700x400')
        obj = student(window)
        window.mainloop()
    else:
        conn.close()
        messagebox.showinfo('error', 'INVALID CREDENTIALS for STUDENT LOGIN')


connect()  # Call connect to create or connect to the database
# Example usage:
# insert(1, 'John Doe', 'password')  # Example of inserting data

# For testing purposes, you can call check or checks functions with hardcoded values
# check('admin_name', 'admin_password')
# checks('student_name', 'student_password')
