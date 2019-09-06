#!/usr/bin/python3
"""module hello flask"""

from flask import Flask, render_template
from models import storage, State
import operator

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states():
    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

app.debug = True
app.run(host='0.0.0.0', port=5000)
