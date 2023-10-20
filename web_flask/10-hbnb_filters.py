#!/usr/bin/python3
"""
This script starts a Flask web application for the HBNB project.
It displays an HTML page for HBNB filters, listing states, cities, and amenities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(error):
    """Closes the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays the HBNB filters HTML page with states, cities, and amenities."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
