#!/usr/bin/python3
"""Starts a Flask web application and defines two routes."""

from flask import Flask

app = Flask(__name__)


# Route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root URL is accessed."""
    return 'Hello HBNB!'


# Route for "/hbnb" with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when the "/hbnb" URL is accessed."""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
