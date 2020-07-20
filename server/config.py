"""Flask server configuration module."""

import os


base_dir = os.path.abspath(os.path.dirname(__file__))


#pylint: disable=too-few-public-methods
class Config:
    """
    Main application config.
    """
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key_for_development")
    SQLALCHEMY_DATABASE_URI = \
        f"sqlite:///{os.path.join(base_dir, 'server.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_GHIBLI_URL = "https://ghibliapi.herokuapp.com"
    FILMS_URL = f"{BASE_GHIBLI_URL}/films"
    PEOPLE_URL = f"{BASE_GHIBLI_URL}/people"
