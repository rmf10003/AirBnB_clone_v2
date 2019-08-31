#!/usr/bin/python3
"""start a Flask web app"""
import flask


app = flask.Flask('web_flask')

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """say hello"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """first flask variable"""
    my_string = 'C %s' % text
    return my_string.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    """first flask variable"""
    my_string = 'Python %s' % text
    return my_string.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def intcheck(n):
    """display "n is a number" only if n is an int"""
    return '%d is a number' % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
