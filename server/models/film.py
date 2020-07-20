"""Film models definition."""

from server import db


table_film_to_character_map = db.Table(
    "film_to_character_map", db.Model.metadata,
    db.Column("film_id", db.Integer,
              db.ForeignKey("film.id"),
              primary_key=True, nullable=False),
    db.Column("character_id", db.Integer,
              db.ForeignKey("character.id"),
              primary_key=True, nullable=False),
)


class Film(db.Model):
    """Defining a film model."""

    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.String(64))
    title = db.Column(db.String(64))
    description = db.Column(db.Text())
    director = db.Column(db.String(64))
    producer = db.Column(db.String(64))
    release_date = db.Column(db.Integer())
    rt_score = db.Column(db.Integer())
    species = db.Column(db.String(128))
    locations = db.Column(db.String(128))
    url = db.Column(db.String(128))

    people = db.relationship(
        "Character", backref="films",
        secondary=table_film_to_character_map
    )

    @classmethod
    def get_or_create_film(cls, film_json):
        """
        Get film info or create a film if it does not exists in the db.

        :param film_json: json object with film fields
        :return: film object instance from the db
        """
        with db.session.no_autoflush:

            film_obj = Film.find_by_film_id(film_json.get("id"))
            if not film_obj:
                film_obj = Film(
                    film_id=film_json.get("id"),
                    title=film_json.get("title"),
                    description=film_json.get("description"),
                    director=film_json.get("director"),
                    producer=film_json.get("producer"),
                    release_date=film_json.get("release_date"),
                    rt_score=film_json.get("rt_score"),
                    url=film_json.get("url"),
                )
                db.session.add(film_obj)
        db.session.commit()
        return film_obj

    @classmethod
    def find_by_film_id(cls, film_id):
        """
        Find db object by its film_id.

        :param film_id: string id of a film
        :return: sqlalchemy query object with first matching result
        """
        return cls.query.filter_by(film_id=film_id).first()

    def __repr__(self):
        return (
            f"<Film id={self.id},  film_id={self.film_id}, title={self.title} "
            f"description={self.description}, director={self.director} "
            f"producer={self.producer} release_date={self.release_date} "
            f"rt_score={self.rt_score} species={self.species} "
            f"locations={self.locations} url={self.url} "
            f"people={[p.id for p in self.people]}>"
        )
