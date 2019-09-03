#!/usr/bin/python3
"""module hello flask"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_t(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd(n):
    if n % 2 is 0:
        number = "even"
    else:
        number = "odd"
    return render_template('6-number_odd_or_even.html', n=n, number=number)


app.debug = True
app.run(host='127.0.0.1', port=5000)
