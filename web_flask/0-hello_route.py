#!/usr/bin/python3
"""start a Flask web app"""
from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """say hello"""
        return 'Hello HBNB!'
