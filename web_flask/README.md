# 0x04. AirBnB clone - Web framework

This project is part of the ALX Africa/Holberton School higher-level programming curriculum, project encompasses a series of tasks and sub-projects, each building on the previous one. Creating a clone of the AirBnB platform. The application is built using Flask, Python, and SQLAlchemy.


## Project Overview

The AirBnB Clone platform main components and features:

1. **Hello World Application:** The project begins with a simple Flask web application that defines a basic route, `/`, which returns the text "Hello HBNB!" when accessed.

2. **Dynamic Routes:** Subsequent tasks introduce dynamic routes, enabling the application to handle URLs with variable components, such as `/c/<text>` and `/python/<text>`. These routes display custom responses based on the provided input.

3. **HTML Templates:** The project progresses to serving HTML pages. The application can render dynamic content, allowing the user to input values and see the result displayed in an HTML format.

4. **Conditional Rendering:** The project extends to include conditional rendering, where the web application displays different content based on conditions. For example, it can determine if a number is even or odd and display the result accordingly.

5. **Database Interaction:** The project starts interacting with a database to retrieve and display data. The application retrieves and displays lists of states, cities, and amenities from a database using Flask and SQLAlchemy.

6. **Filters and Templates:** The final stages introduce more complex features. Users can filter results based on states, cities, and amenities. The application loads dynamic content from a database and displays it in a user-friendly interface. It also includes styles, images, and improved HTML templates to create an enhanced user experience.


## Project Tasks

| File Name                 | Description                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------|
| `0-hello_route.py`        | A simple Flask web application that defines a single route `/` that returns "Hello HBNB!"    |
| `1-hbnb_route.py`         | A Flask web application with a single route `/hbnb` that returns "HBNB"                        |
| `2-c_route.py`            | A Flask web application with a route `/c/<text>` that returns "C" followed by the value of `<text>` |
| `3-py_route.py`           | A Flask web application with a route `/python/<text>` that returns "Python" followed by the value of `<text>` |
| `4-number_route.py`       | A Flask web application with a route `/number/<n>` that returns "n is a number" if `<n>` is an integer |
| `5-number_template.py`    | A Flask web application that serves an HTML page at route `/number_template/<n>` if `<n>` is an integer |
| `6-number_odd_or_even.py` | A Flask web application that serves an HTML page displaying whether `<n>` is even or odd at route `/number_odd_or_even/<n>` if `<n>` is an integer |
| `7-states_list.py`        | A Flask web application that displays a list of states retrieved from the storage engine |
| `8-cities_by_states.py`   | A Flask web application that displays a list of cities by state retrieved from the storage engine |
| `9-states.py`             | A Flask web application that displays a list of states and their cities or a "Not found" message |
| `10-hbnb_filters.py`      | A Flask web application that displays an HTML page with filters for states, cities, and amenities |
| `10-hbnb_filters.html`    | An HTML template file for the HBNB filters page |
| `static/`                 | A folder containing static files such as CSS and images for the project |
| `templates/`              | A folder containing HTML templates used in the Flask application |

## Usage

1. Make sure you have Python, Flask, SQLAlchemy, and other dependencies installed.
2. Clone this repository.
3. Run the desired Python script to start the Flask application, e.g., `python3 10-hbnb_filters.py`.
4. Open a web browser and access the application at `http://0.0.0.0:5000/`.

Enjoy exploring the AirBnB Clone project!

## Author

[Github](https://github.com/lebogangolifant)
