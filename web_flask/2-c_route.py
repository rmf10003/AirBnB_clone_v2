
#!/usr/bin/python3
"""start a Flask web app"""
import flask


app = flask.Flask(__name__)


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
