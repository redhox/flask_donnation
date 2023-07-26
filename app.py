from flask import Flask, render_template , request
import jinja2
import data
from dotenv import load_dotenv
import os
from data import set_donateur,get_donateur
load_dotenv()
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chaque_don_compte')
def formulaire():
    
    return render_template('page_formulaire.html')

@app.route('/merci', methods=['POST'])
def remerciment():
    nom= request.form.get('nom')
    prenom= request.form.get('prenom')
    don= request.form.get('don')
    message= request.form.get('message')
    print(f"entre={nom},{prenom},{don},{message}")
    set_donateur(nom, prenom,don,message)
    return render_template('remerciment.html',nom=nom,prenom=prenom,don=don,message=message,donateur=get_donateur())

if __name__ == "__main__":
    app.run(debug=True)