from flask import Flask 
app = Flask(__name__)
#Multiple routes for single function 
@app.route('/')
@app.route('/home')
def home():
    return "Welcome"
@app.route('/profile/')
@app.route('/userprofile/')
def wish():
    return "hello good morning"
#Static routing ==> /name/meghana
#Dyanmic routing ==> /name/<name>

@app.route('/name/<name>')
def name(name):
     return f'hello <b>{name}</b>'
@app.route('/profile/course/<course>')
def name_course(course):
     return f'<b><i>hello this is {course}</i></b>'
@app.route('/student/<int:id>')
def std_id(id):
     return f'student id is {id}'
@app.route('/studentattnd/<float:att>')
def std_attendance(att):
     return f'student attendance percentage  is <b>{att}</b>'
@app.route('/file/<path:file_name>')
def file(file_name):
     return f'File name is <b>{file_name}</b>'
#Universal Unique Identifier(UUID)
@app.route('/student_id/<uuid:s_id>')
def u_stud_id(s_id):
     return f'Student uuid id <b>{s_id}</b>'
if __name__ == "__main__":
      app.run(host='0.0.0.0',port=5009,debug=True)