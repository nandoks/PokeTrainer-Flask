# PokeTrainer-Flask
This is a python/flask exercice, i got the idea from https://www.pokemongofriendcodes.com/, it uses python,flask, MySql.
This is itended as a execice to learn how to communicate with a MySQL DB with python and flask.
Front end is not important for this project, it is a backend exercice so i didn't give too much attention to it
The idea behind it is that a Pokemon Go Player can share their trainer code with other trainers, the code, team and country is added to the DB, trainers can add the code again in 24h, so the name will go back to the beginning of the list, the list if fetch on the DB by latest added. if the trainercode already exists on the DB the date is updated otherwise it is added to the DB;



Libraries needed:
Flask==0.12.2       
Flask-MySQLdb==0.2.0
