from flask import Flask,render_template,redirect,url_for 
import uuid
app = Flask(__name__)
@app.route('/')
def home():
    return redirect(url_for('index_page'))
@app.route('/subject/<string:sub>/<float:marks>')
def details(sub,marks):
    return f"Your subject is <b>{sub}</b> <br> Your score is <b>{marks}</b>"
@app.route('/generate')
def generate():
    id =   uuid.uuid4().hex
    return f'Your id is <b>{id}</b>'
@app.route('/index')
def index_page():
    return render_template('index.html')
@app.route('/about')
def about_page():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000,debug=True)