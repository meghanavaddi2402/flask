from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/getData', methods=['GET'])
def getData():
    name = request.args.get('name')
    batchno = request.args.get('batchno')

    return jsonify({
        'name': name,
        'batchno': batchno
    })

@app.route('/postData', methods=['POST'])
def postData():
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Please send valid JSON data'}), 400

    name = data.get('name')
    skills = data.get('skills')

    return jsonify({
        'name': name,
        'skills': skills
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)