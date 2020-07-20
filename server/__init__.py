"""Creating and initializing the server's modules."""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from server.config import Config
from server.get_latest_movies_info import UpdateMoviesInfo


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Init logger class
movies_info = UpdateMoviesInfo()


def create_app(testing_config=None):
    """
    Crete, configure and setup the app.

    :param dict testing_config: will be used for defining flask scope
    :return: None
    """
    # pylint: disable=import-outside-toplevel, unused-import
    from server.scheduler import init_scheduler
    from server.api import movies
    from server.models import film, character

    if testing_config:
        # If passed testing config we use it
        app.config.from_mapping(testing_config)
    else:
        # Use dev config (default)
        app.config.from_object(Config)

    movies_info.init_app(app)
    init_scheduler()
    db.init_app(app)
    with app.app_context():
        db.create_all()
