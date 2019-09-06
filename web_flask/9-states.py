#!/usr/bin/python3
"""start a Flask web app with specs"""
from flask import Flask, render_template
from models import storage


app = Flask('web_flask')


app.url_map.strict_slashes = False

@app.route('/states', defaults={'id': None})
@app.route('/states/<string:id>')
def states(id):
    """render html of states list"""
    return render_template(
        '9-states.html',
        header='States',
        state_dict=storage.all('State'),
        s_id=id
    )

@app.teardown_appcontext
def app_close(a):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
