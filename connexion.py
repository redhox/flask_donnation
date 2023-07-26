import mysql.connector as mysqlpyth
from dotenv import load_dotenv

load_dotenv()
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
database = os.getenv('database')


bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = mysqlpyth.connect(user='root', password='example', host='localhost',
    port="3307", database='flask_blog')
    cursor = bdd.cursor()

def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()
