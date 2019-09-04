#!/usr/bin/python3
"""module hello flask"""

from flask import Flask, render_template
from models import storage, State
import operator

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    states = storage.all(State)
    states_l = []
    for key, values in states.items():
        tup = (values.id, values.name)
        states_l.append(tup)
        states_l.sort(key=operator.itemgetter(1))
    return render_template('7-states_list.html', states=states_l)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

app.debug = True
app.run(host='0.0.0.0', port=5000)
