#!/usr/bin/python3
"""module hello flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"

app.debug = True
app.run(host='0.0.0.0', port=5000)
app.url_map.strict_slashes = False
