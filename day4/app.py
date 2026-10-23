
from flask import Flask,render_template,url_for,request,redirect
import uuid
app = Flask(__name__)
@app.route('/')
def home():    
    return redirect(url_for('about_page'))
@app.route('/<string:name>')
def std_home(name):
    return f"Welcome <b>{name}</b>"
@app.route('/studentid/<int:id>')
def std_id(id):
     return f"Hello Your ID id {id}"
@app.route('/attendance/<float:att>')
def std_attendance(att):
     return f'student attendance percentage  is <b>{att}</b>'
@app.route('/file/<path:file_name>')
def file(file_name):
     return f'File name is <b>{file_name}</b>'
@app.route('/skills/<string:s1>/<string:s2>')
def skill(s1,s2):
    return f"Your skills are <br> <b>{s1}</b><br><b>{s2}</b>"
@app.route('/generate')
def generate():
    id = uuid.uuid4().hex
    #print(id)
    return f'Generated id is {id}'
@app.route('/index')
def index_page():
     return render_template('index.html')
@app.route('/about')
def about_page():
     return render_template('about.html')
if __name__ == "__main__":
      app.run(host='0.0.0.0',port=5009,debug=True)