"""Character models definition."""

from server import db


class Character(db.Model):
    """Defining a character model."""

    __tablename__ = "character"

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.String(64))
    name = db.Column(db.String(128))
    gender = db.Column(db.String(8))
    age = db.Column(db.String(32))
    eye_color = db.Column(db.String(16))
    hair_color = db.Column(db.String(16))
    species = db.Column(db.String(128))
    url = db.Column(db.String(128))

    @classmethod
    def get_or_create_character(cls, character_json):
        """
        Get character info or create a character if it does not exists in
        the db yet.

        :param film_json: json object with film fields
        :return: film object instance from the db
        """
        with db.session.no_autoflush:
            character_obj = Character.find_by_character_id(
                character_json.get("id"))
            if not character_obj:
                character_obj = Character(
                    character_id=character_json.get("id"),
                    name=character_json.get("name"),
                    gender=character_json.get("gender"),
                    age=character_json.get("age"),
                    eye_color=character_json.get("eye_color"),
                    hair_color=character_json.get("hair_color"),
                    species=character_json.get("species"),
                    url=character_json.get("url"),
                )
                db.session.add(character_obj)
        db.session.commit()
        return character_obj

    @classmethod
    def find_by_character_id(cls, character_id):
        """
        Find db object by its film_id.

        :param character_id: string id of a character
        :return: sqlalchemy query object with first matching result
        """
        return cls.query.filter_by(character_id=character_id).first()

    def __repr__(self):
        return (
            f"<Character id={self.id},  character_id={self.character_id}, "
            f"name={self.name} gender={self.gender}, age={self.age} "
            f"eye_color={self.eye_color} hair_color={self.hair_color} "
            f"species={self.species} url={self.url} "
            f"films={[f.id for f in self.films]}>"
        )
