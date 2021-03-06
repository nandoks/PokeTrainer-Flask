from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
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
    if(not code.isdecimal()):
        flash('trainer code must be only made of numbers')

    t = trainerDAO.select_by_id(code)
    if(t.dateInserted - datetime.now()):
        flash('trainer must wait 24h before sending their code again')
    else:
        team = request.form['team']
        country = request.form['country']
        trainer = Trainer(code, team, country)
        trainerDAO.insert(trainer)
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search():
    countries = contryDAO.select_all()
    trainers = trainerDAO.select_with_filter(request.args.get('country'), request.args.get('team'))
    return render_template('index.html', titulo='Trainers', trainers=trainers, countries=countries)




app.run(debug=True)
