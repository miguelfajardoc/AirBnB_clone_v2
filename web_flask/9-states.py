#!/usr/bin/python3
"""module hello flask"""

from flask import Flask, render_template
from models import storage, State
import operator

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': '0'})
@app.route('/states/<id>')
def states(id):
    states = storage.all(State)
    if id == '0':
        flag = '1'
    else:
        flag = '0'

    for key, state in states.items():
        if state.id == id:
            flag = '1'
            break

    return render_template('9-states.html', states=states, f_id=id, flag=flag)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()

app.debug = True
app.run(host='0.0.0.0', port=5000)
