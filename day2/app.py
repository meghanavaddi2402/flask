from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    """home page """
    return "Vachindi andi vyari....!!!"
@app.route('/maggi')
def me():
    """about me"""
    return "idi nene"
@app.route('/me')
def profile():
    """profile"""
    return "I'm Meghana....."

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)