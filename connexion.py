import mysql.connector as mysqlpyth
from dotenv import load_dotenv
import os




bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    load_dotenv()
    bdd = mysqlpyth.connect(user = os.getenv('USER_BDD'),password = os.getenv('PASSWORD'),host =os.getenv('HOST'),port = os.getenv('PORT'),database = os.getenv('DATABASE'))
    cursor = bdd.cursor()
    return bdd, cursor

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()
