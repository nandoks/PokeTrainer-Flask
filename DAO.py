from models import Trainer, Country
from datetime import datetime

SQL_INSERT_TRAINER = 'INSERT into trainer (code, team, dateinserted, country) values (%s,%s,%s,%s);'
SQL_SELECT_ALL_TRAINERS = 'SELECT * from Trainer inner join countries on Trainer.country = Countries.threecode order by dateinserted desc'
SQL_SELECT_ALL_COUNTRIES = 'SELECT * from Countries'



class TrainerDAO:
    def __init__(self,db):
        self._db = db
    
    def insert(self, trainer):
        cursor = self._db.connection.cursor()

        cursor.execute(SQL_INSERT_TRAINER, (trainer.code, trainer.team,
            trainer.dateInserted, trainer.country))
        self._db.connection.commit()

    def select_all(self):
        cursor = self._db.connection.cursor()
        cursor.execute(SQL_SELECT_ALL_TRAINERS)
        result = list_trainers(cursor.fetchall())
        return result

class CountryDAO:
    def __init__(self, db):
        self._db = db

    def select_all(self):
        cursor = self._db.connection.cursor()
        cursor.execute(SQL_SELECT_ALL_COUNTRIES)
        result = list_countries(cursor.fetchall())
        return result


def list_trainers(trainers):
    def create_trainer_from_tuple(trainers):
        return Trainer(trainers[0], trainers[1], trainers[2], trainers[3])
    return list(map(create_trainer_from_tuple, trainers))

    
def list_countries(countries):
    def create_countries_from_tuple(countries):
        return Country(countries[0], countries[1])
    return list(map(create_countries_from_tuple, countries))