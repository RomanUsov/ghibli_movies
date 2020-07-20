"""General fixtures for all test suite."""

import os
import pytest

from flask_sqlalchemy import SQLAlchemy
from server import app, create_app


base_dir = os.path.abspath(os.path.dirname(__file__))
test_config = {
    "SECRET_KEY": os.environ.get("SECRET_KEY", "secret_key_for_development"),
    "TESTING": True,
    "BASE_GHIBLI_URL": "https://ghibliapi.herokuapp.com",
    "FILMS_URL": "https://ghibliapi.herokuapp.com/films",
    "PEOPLE_URL": "https://ghibliapi.herokuapp.com/people",
    "SQLALCHEMY_DATABASE_URI":
        f"sqlite:///{os.path.join(base_dir, 'test.db')}",
}


@pytest.fixture(scope='session')
def flask_app():
    """A fixture that initializes the flask app."""
    create_app(testing_config=test_config)

    db_instance = SQLAlchemy(app)
    db_instance.init_app(app)

    with app.app_context():
        db_instance.create_all()
        yield app
        db_instance.drop_all()


# pylint: disable=redefined-outer-name, invalid-name, unused-argument
@pytest.fixture(scope='session')
def db(flask_app):
    """A fixture that initializes the db."""
    # pylint: disable=import-outside-toplevel
    from server import db as db_instance
    yield db_instance


# pylint: disable=redefined-outer-name
@pytest.fixture(scope='session')
def flask_client(flask_app):
    """A fixture that initializes flask's testing client."""
    with flask_app.test_client() as client:
        yield client
