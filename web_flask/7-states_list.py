#!/usr/bin/python3
"""start a Flask web app with specs"""
from flask import Flask, render_template
from models import storage


app = Flask('web_flask')


@app.route('/states_list', strict_slashes=False)
def states_list():
    """render html of states list"""
    return render_template(
        '7-states_list.html',
        header='States',
        state_dict=storage.all('State')
    )


@app.teardown_appcontext
def app_close(a):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
