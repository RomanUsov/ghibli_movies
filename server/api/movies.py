"""Defining the task data package resources."""

from flask import render_template

from server import app
from server.models.film import Film


@app.route("/")
def main_page():
    """
    A placeholder page to notify users about the movies page.

    :return: main.html page
    """
    return render_template("main.html", title="Main page")


@app.route("/movies")
def movies_page():
    """
    List of all movies from the Ghibli API.  # db?

    :return: index.html page
    """
    data_objects = Film.query.all()
    return render_template(
        "movies.html", title="Studio Ghibli movies", data=data_objects)
