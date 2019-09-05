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
    cities_by_states = {}
    iter = 0
    for state in states:
        cities_by_states[str(states[state].id)] = states[state].cities

    states_l = []
    for key, values in states.items():
        tup = (values.id, values.name)
        states_l.append(tup)
        states_l.sort(key=operator.itemgetter(1))
    return render_template('8-cities_by_states.html', states=states_l,
                           cities=cities_by_states)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

app.debug = True
app.run(host='0.0.0.0', port=5000)
