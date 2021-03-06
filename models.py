from datetime import datetime

class Trainer:

    def __init__(self, code, team, country, date=datetime.now()):
        self._code = code
        self._team = team
        self._country = country
        self._dateInserted = date

    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, code):
        self._code = code

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self,team):
        self._team = team
    
    @property
    def country(self,):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country

    @property
    def dateInserted(self):
        return self._dateInserted

class Country:
    def __init__(self, threecode, name):
        self._threecode = threecode
        self._name = name

    @property
    def threecode(self):    
        return self._threecode
    
    @threecode.setter
    def threecode(self, code):
        self.threecode = code

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name