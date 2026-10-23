from flask import Flask, render_template, url_for,request,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/student", methods=["GET"])
def get_student():
    name = request.args.get("name")
    batchno = request.args.get("batchno")

    return jsonify({
        "name": name,
        "batchno": batchno
    })


@app.route("/skills", methods=["POST"])
def get_skills():
    data = request.get_json()

    name = data.get("name")
    skills = data.get("skills")

    return jsonify({
        "name": name,
        "skills": skills
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port = 5002,debug=True)