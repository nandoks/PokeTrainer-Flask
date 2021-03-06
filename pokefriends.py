from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
import pyodbc
from models import Trainer, Country
from DAO import TrainerDAO, CountryDAO
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'nandoks'

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "admin"
app.config['MYSQL_DB'] = "pokefriends"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

trainerDAO = TrainerDAO(db)
contryDAO = CountryDAO(db)

@app.route('/')
def index():
    countries = contryDAO.select_all()
    trainers = trainerDAO.select_all()
    return render_template('index.html', titulo='Trainers', trainers=trainers, countries=countries)


@app.route('/addTrainer', methods=['POST', ])
def addTrainer():
    code = request.form['trainerCode'].replace(' ', '')
    if(len(code) != 12):
        flash('trainer code must contain 12 numbers')
        return redirect(url_for('index'))
    if(not code.isdecimal()):
        flash('trainer code must be only made of numbers')
        return redirect(url_for('index'))

    team = request.form['team']
    country = request.form['country']
    trainer = Trainer(code, team, country)
    trainerDAO.insert(trainer)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in listaUsuarios:
        usuario = listaUsuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' Logado com sucesso')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Ocorreu um erro no login ou senha')
        return redirect(url_for('login'))


@app.route('/logout')
def desloga():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect(url_for('index'))


app.run(debug=True)
