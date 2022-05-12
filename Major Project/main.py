import sqlite3
import datetime
from bottle import run, route, view, static_file, get, template, request, redirect, app

# loads css
@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')

    #when pressed, redirected to login page
@route ('/login')
def login_redirect():
    redirect('/login')

#load login page
@route('/')
@view('login')
def login():
    return dict(incorrect="none")

#checking database for valid login
def check_login(username,password):
    conn = sqlite3.connect('logindetails.db')
    c = conn.cursor()
    c.execute("SELECT username, successful_logins FROM logindetails WHERE username LIKE ? AND password LIKE ?", (username, password))
    result = c.fetchall()


#view login formand check login before continuing to homepage
@route('/login', method='POST')
def do_login():
    global username
    username = request.forms.get('username').strip()
    password = request.forms.get('password').strip()

    #show 'incorrect' message if password is incorrect
    if check_login(username, password):
        return redirect('/index')
    else:
        return template('login', incorrect="block")


@route('/login', method = 'GET')
def create_table_name():
    return template('create_new.tpl')

TableName = ''

import re
@route('/login', method = 'POST')
def create_table():
    global TableName
    TableName = request.forms.get('username').strip()
    conn = sqlite3.connect("TheTable.db")


run(host='127.1.0.1', port=8080, reloader=True, debug=True)