#!/usr/bin/python3
"""module hello flask"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def C_is_fun(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def Python_is_magic(text):
    text = text.replace('_', ' ')
    return "Python {}".format(text)

app.debug = True
app.run(host='0.0.0.0', port=5000)
