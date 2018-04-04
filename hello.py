from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hey kobe!'


@app.route('/tuna')
def tuna():
    return '<h2>Hey shahar!</h2>'
