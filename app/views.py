# coding=utf-8
from flask import render_template, redirect, session, url_for, request
from dateutil.relativedelta import relativedelta
from datetime import datetime
from app import app
import time
import workWithDb

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    date = time.strftime("%Y-%m-%d", time.localtime())
    allTables = workWithDb.getTables(date)
    if request.method == 'POST':
        workWithDb.setOrder(request.form['name'], request.form['email'], request.form['date'], request.form['tables'])

    return render_template("main_page.html", tables = allTables, date =date)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # print request.form['username']
    if request.method == 'POST':
        if workWithDb.isUserExists(request.form['username'], request.form['password']) is True:
            session['username'] = request.form['username']
            return redirect(url_for('create_rest_hall'))
        else:
            error = 'Invalid login combination'
            return render_template("login.html", error=error)

    return render_template("login.html", error=error)

@app.route('/create_rest_hall', methods = ['GET', 'POST'])
def create_rest_hall():
    error = None
    date = time.strftime("%Y-%m-%d", time.localtime())
    allTables = workWithDb.getTables(date)
    if 'username' in session:
        if request.method == 'POST':
            workWithDb.setTable(request.form['seats'], request.form['form'], request.form['coordLen'],
                                request.form['coordWidth'], request.form['sizeLen'], request.form['sizeWidth'])
        return render_template('create_rest_hall.html', error = error, tables = allTables)
    else:
        return render_template("login.html", error=error)
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/showdate', methods=['GET', 'POST'])
def showdate():
    if request.method == 'POST':
        date = request.form['date']
        allTables = workWithDb.getTables(date)
        return render_template("main_page.html", tables=allTables, date = date)

    date = time.strftime("%Y-%m-%d", time.localtime())
    allTables = workWithDb.getTables(date)
    return render_template("main_page.html", tables=allTables, date=date)

@app.route('/nextday', methods=['GET', 'POST'])
def nextday():
    if request.method == 'POST':
        date = request.form['date']
        date = date.split('-')
        date = datetime(int(date[0]), int(date[1]), int(date[2]))
        date_next = date + relativedelta(days=1)
        allTables = workWithDb.getTables(date_next.strftime("%Y-%m-%d"))
        return render_template("main_page.html", tables=allTables, date = date_next.strftime("%Y-%m-%d"))


@app.route('/previousday', methods=['GET', 'POST'])
def previousday():
    if request.method == 'POST':
        date = request.form['date']
        date = date.split('-')
        date = datetime(int(date[0]), int(date[1]), int(date[2]))
        date_prev = date - relativedelta(days=1)
        date_prev = date_prev.strftime("%Y-%m-%d")
        allTables = workWithDb.getTables(date_prev)
        return render_template("main_page.html", tables=allTables, date = date_prev)



























