"""A module related to movie information tasks."""

import logging
import os
import requests


class UpdateMoviesInfo:
    """Class for updating information about movies."""

    def __init__(self):
        self.base_ghibli_url = ""
        self.films_url = ""
        self.people_url = ""

    def init_app(self, app):
        """
        Setup initial field from app.config.

        :param app: object current flask app
        :return: None
        """
        self.base_ghibli_url = app.config.get("BASE_GHIBLI_URL")
        self.films_url = app.config.get("FILMS_URL")
        self.people_url = app.config.get("PEOPLE_URL")

    # pylint: disable=no-self-use
    def get_url(self, url):
        """
        Try to get given url using http GET method.

        :param url: string URL
        :return: json representation of the request results or empty list
        """
        request = requests.get(url)

        try:
            request.raise_for_status()
            return request.json()
        # pylint: disable=invalid-name
        except requests.exceptions.HTTPError as e:
            logging.warning(
                "Get latest movies info failed because of the error: %s", e)
            return []

    # pylint: disable=import-outside-toplevel
    def update_movies_info(self):
        """
        Try to get info about films and characters from the Ghibli API.

        The method performs GET queries to /people and /films urls, processes
        data, and saves received films and people to the db.
        :return:  None
        """
        print("*"*60, flush=True)
        from server.models.character import Character
        from server.models.film import Film

        films_json = self.get_url(self.films_url)
        films_dict = {f["id"]: Film.get_or_create_film(f) for f in films_json}
        people_json = self.get_url(self.people_url)
        for character in people_json:
            character_obj = Character.get_or_create_character(character)
            if not character.get("films"):
                print(character)
                print(character_obj)
            character_obj.films = [
                films_dict[os.path.split(film_url)[-1]]
                for film_url in character.get("films", [])
            ]
