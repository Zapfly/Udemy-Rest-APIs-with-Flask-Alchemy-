from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.google.com/' the '/' is the homepage
def home():
    return "Hello, world!"

app.run(port=3000)