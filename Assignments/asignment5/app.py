
from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"id": 101, "name": "Meghana", "percentage": 92},
    {"id": 102, "name": "Meena", "percentage": 85},
    {"id": 103, "name": "Ankitha", "percentage": 78},
    {"id": 104, "name": "Vandana", "percentage": 65},
    {"id": 105, "name": "Sravathi", "percentage": 88},
    {"id": 106, "name": "Kiran", "percentage": 72},
    {"id": 107, "name": "Charan", "percentage": 95},
    {"id": 108, "name": "Rahul", "percentage": 55},
    {"id": 109, "name": "Anjali", "percentage": 81},
    {"id": 110, "name": "Suresh", "percentage": 35}
]


@app.route('/')
def home():
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
