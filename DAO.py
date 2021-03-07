from models import Trainer, Country
from datetime import datetime

SQL_INSERT_TRAINER = 'INSERT into trainer (code, team, country, dateinserted) values (%s,%s,%s,%s);'
SQL_SELECT_ALL_TRAINERS = 'SELECT code, team, countries.name, dateinserted from Trainer inner join countries on Trainer.country = Countries.threecode order by dateinserted desc'
SQL_SELECT_ALL_COUNTRIES = 'SELECT * from Countries'
SQL_SELECT_TRAINERS_WITH_FILTER = 'SELECT code, team, countries.name, dateinserted from Trainer inner join countries on Trainer.country = Countries.threecode  where country=%s and team=%s order by dateinserted desc'
SQL_SELECT_BY_ID = 'SELECT code, team, countries.name, dateinserted from Trainer inner join countries on Trainer.country = Countries.threecode where code=%s'
SQL_UPDATE_TRAINER = 'UPDATE trainer set dateInserted=%s, team=%s, country=%s where code=%s'
class TrainerDAO:
    def __init__(self,db):
        self._db = db
    
    def insert(self, trainer):
        cursor = self._db.connection.cursor()

        if(self.select_by_id(trainer.code) is not None):
            cursor.execute(SQL_UPDATE_TRAINER, (trainer.dateInserted, trainer.team, trainer.country, trainer.code))
        else:
            cursor.execute(SQL_INSERT_TRAINER, (trainer.code, trainer.team,
                trainer.country, trainer.dateInserted))
        self._db.connection.commit()

    def select_all(self):
        cursor = self._db.connection.cursor()
        cursor.execute(SQL_SELECT_ALL_TRAINERS)
        result = list_trainers(cursor.fetchall())
        return result

    def select_with_filter(self, country, team):
        cursor = self._db.connection.cursor()
        cursor.execute(SQL_SELECT_TRAINERS_WITH_FILTER, (country, team))
        result = list_trainers(cursor.fetchall())
        return result

    def select_by_id(self, code):
        cursor = self._db.connection.cursor()
        cursor.execute(SQL_SELECT_BY_ID, [code])
        result = cursor.fetchone()
        if(result is not None):
            return Trainer(result[0], result[1], result[2], result[3])
        else:
            return None
        

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