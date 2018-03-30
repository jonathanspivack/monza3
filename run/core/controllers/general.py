#!/usr/bin/env python3

from flask import Blueprint, render_template, request
import sqlite3

controller = Blueprint('general', __name__)

@controller.route('/', methods=['GET'])
def show_frontpage():
	return render_template('index.html')

@controller.route('/login',methods=['GET','POST'])
def login():
        username = request.form['username']
        password = request.form['password']
        if username != 'mellon@gmail.com':
                return "not a user!!"
        print(username)
        print(password)
        credentials = auth(username,password)
        if credentials:
            return render_template('main_page.html')
        return "wrong password!!!"


@controller.route('/buy',methods=['GET'])
def buy():
        return 'buy this!'






def auth(username,password):
        connection = sqlite3.connect('master.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,))
        user = result.fetchone()
        connection.commit()
        connection.close()

        if user[1] == password:
            return True
        else:
            return False
