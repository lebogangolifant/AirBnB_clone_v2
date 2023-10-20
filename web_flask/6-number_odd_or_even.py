#!/usr/bin/python3
"""Starts a Flask web application and defines seven routes."""

from flask import Flask, render_template

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


# Route for "/c/<text>" with strict_slashes=False
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ', followed by the value of the "text" variable.
    Replace underscore "_" symbols with spaces.
    """
    return 'C ' + text.replace('_', ' ')


# Route for "/python/<text>" with strict_slashes=False
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Display 'Python ', followed by the value of the "text" variable.
    If no "text" is provided, use the default value "is cool."
    Replace underscore "_" symbols with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


# Route for "/number/<n>" with strict_slashes=False
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display 'n is a number' only if n is an integer.
    """
    return '{} is a number'.format(n)


# Route for "/number_template/<n>" with strict_slashes=False
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display an HTML page with 'Number: n' inside an H1 tag if n is an integer.
    """
    return render_template('6-number_template.html', number=n)


# Route for "/number_odd_or_even/<n>" with strict_slashes=False
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML page with 'Number: n is even|odd'
    inside an H1 tag if n is an integer.
    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               number=n, odd_even='even')
    else:
        return render_template('6-number_odd_or_even.html',
                               number=n, odd_even='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
