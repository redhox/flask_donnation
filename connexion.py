import mysql.connector as mysqlpyth
from dotenv import load_dotenv
import os




bdd = None
cursor = None

def connexion():
    global bdd
    global cursor
    load_dotenv()
    bdd = mysqlpyth.connect(user = 'root',password = 'example',host ='localhost',port = '3307',database = 'donnation')
    cursor = bdd.cursor()
    return bdd, cursor

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()
