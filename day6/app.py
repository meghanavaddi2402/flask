
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = 20
    student_details = [
        {
            "id": 1,
            "name": "meghana"
        },
        {
            "id": 2,
            "name": "meena"
        }
    ]

    return render_template('index.html', d=data, m=student_details)

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

