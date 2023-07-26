from flask import Flask, render_template , request
import data
app = Flask(__name__)
@app.route('/')
def index():
    posts = data.lire_posts()
    return render_template('index.html',port=posts)

@app.route('/truc')
def truc():
    name="feur"
    return render_template('truc.html',name=name)

@app.route('/formu', methods=['POST'])
def form_handler():
    name = request.form.get('name')
    print(name)
    return render_template('truc.html',name=name)

if __name__ == "__main__":
    app.run(debug=True)