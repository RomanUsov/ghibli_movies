"""Fixtures for task_data test suite."""

import pytest

from server import movies_info
from server.models.film import Film
from server.models.character import Character


def get_character_data():
    """Defining a list of data that can be used to create a character."""
    characters = [
        {
            "character_id": "7151abc6-1a9e-4e6a-9711-ddb50ea572ec",
            "name": "Jiji",
            "gender": "Male",
            "age": "NA",
            "eye_color": "Black",
            "hair_color": "Black",
            "species": "https://ghibliapi.herokuapp.com/species/"
                       "603428ba-8a86-4b0b-a9f1-65df6abef3d3",
            "url": "https://ghibliapi.herokuapp.com/people/"
                   "7151abc6-1a9e-4e6a-9711-ddb50ea572ec",
        },
        {
            "character_id": "d39deecb-2bd0-4770-8b45-485f26e1381f",
            "name": "Totoro",
            "gender": "NA",
            "age": "",
            "eye_color": "Grey",
            "hair_color": "Grey",
            "species": "https://ghibliapi.herokuapp.com/species/"
                       "74b7f547-1577-4430-806c-c358c8b6bcf5",
            "url": "https://ghibliapi.herokuapp.com/people/"
                   "d39deecb-2bd0-4770-8b45-485f26e1381f",
        },
        {
            "character_id": "591524bc-04fe-4e60-8d61-2425e42ffb2a",
            "name": "Chu Totoro",
            "gender": "NA",
            "age": "",
            "eye_color": "Black",
            "hair_color": "Blue",
            "species": "https://ghibliapi.herokuapp.com/species/"
                       "74b7f547-1577-4430-806c-c358c8b6bcf5",
            "url": "https://ghibliapi.herokuapp.com/people/"
                   "591524bc-04fe-4e60-8d61-2425e42ffb2a",
        },
        {
            "character_id": "c491755a-407d-4d6e-b58a-240ec78b5061",
            "name": "Chibi Totoro",
            "gender": "NA",
            "age": "",
            "eye_color": "Black",
            "hair_color": "White",
            "species": "https://ghibliapi.herokuapp.com/species/"
                       "74b7f547-1577-4430-806c-c358c8b6bcf5",
            "url": "https://ghibliapi.herokuapp.com/people/"
                   "c491755a-407d-4d6e-b58a-240ec78b5061",
        },
    ]

    return characters


# pylint: disable=redefined-outer-name
def get_film_data(multiple_characters):
    """Defining a list of data that can be used to create a film."""
    films = [
        {
            "film_id": "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
            "title": "My Neighbor Totoro",
            "description": "Two sisters move to the country with their "
                           "father in order to be closer to their hospitalized"
                           " mother, and discover the surrounding trees are "
                           "inhabited by Totoros, magical spirits of the "
                           "forest. When the youngest runs away from home, "
                           "the older sister seeks help from the spirits "
                           "to find her.",
            "director": "Hayao Miyazaki",
            "producer": "Hayao Miyazaki",
            "release_date": 1988,
            "rt_score": 93,
            "url": "https://ghibliapi.herokuapp.com/films/"
                   "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
            "people": multiple_characters[1:]
        },
        {
            "film_id": "ea660b10-85c4-4ae3-8a5f-41cea3648e3e",
            "title": "Kiki's Delivery Service",
            "description": "Kiki's Delivery Service	A young witch, on her "
                           "mandatory year of independent life, finds fitting"
                           " into a new community difficult while she supports"
                           " herself by running an air courier service.",
            "director": "Hayao Miyazaki",
            "producer": "Hayao Miyazaki",
            "release_date": 1989,
            "rt_score": 96,
            "url": "https://ghibliapi.herokuapp.com/films/"
                   "ea660b10-85c4-4ae3-8a5f-41cea3648e3e",
            "people": [multiple_characters[0]]
        },
    ]

    return films


# pylint: disable=redefined-outer-name
# @pytest.fixture(scope='session')
# def monkeypatch_session():
#     """
#         Monkeypatch monkeypatch to support session scope.
#         Why? https://github.com/pytest-dev/pytest/issues/1872
#     """
#     # pylint: disable=import-outside-toplevel
#     from _pytest.monkeypatch import MonkeyPatch
#     monkeypatch_object = MonkeyPatch()
#     yield monkeypatch_object
#     monkeypatch_object.undo()


@pytest.fixture(scope='function')
def mock_get_url(monkeypatch):
    """
        Mock requests object's method get() to prevent real request sending.
    """

    # pylint: disable=unused-argument
    def get_url(*args, **kwargs):
        films_json = [{
            'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe',
            'title': 'Castle in the Sky',
            'description': "The orphan Sheeta inherited a mysterious crystal "
                           "that links her to the mythical sky-kingdom of "
                           "Laputa. With the help of resourceful Pazu and a "
                           "rollicking band of sky pirates, she makes her way "
                           "to the ruins of the once-great civilization. "
                           "Sheeta and Pazu must outwit the evil Muska, who "
                           "plans to use Laputa's science to make himself "
                           "ruler of the world.",
            'director': 'Hayao Miyazaki',
            'producer': 'Isao Takahata',
            'release_date': '1986',
            'rt_score': '95',
            'people': ['https://ghibliapi.herokuapp.com/people/'],
            'species': [
                'https://ghibliapi.herokuapp.com/species/'
                'af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'
            ],
            'locations': ['https://ghibliapi.herokuapp.com/locations/'],
            'vehicles': ['https://ghibliapi.herokuapp.com/vehicles/'],
            'url': 'https://ghibliapi.herokuapp.com/films/'
                   '2baf70d1-42bb-4437-b551-e5fed5a87abe'
        }]
        characters_json = [{
            "id": "40c005ce-3725-4f15-8409-3e1b1b14b583",
            "name": "Colonel Muska",
            "gender": "Male",
            "age": "33",
            "eye_color": "Grey",
            "hair_color": "Brown",
            "films": [
                "https://ghibliapi.herokuapp.com/films/"
                "2baf70d1-42bb-4437-b551-e5fed5a87abe"
            ],
            "species": "https://ghibliapi.herokuapp.com/"
                       "species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
            "url": "https://ghibliapi.herokuapp.com/people/"
                   "40c005ce-3725-4f15-8409-3e1b1b14b583"
        }]
        return films_json if args[0].endswith("films") else characters_json

    monkeypatch.setattr(movies_info, "get_url", get_url)


# pylint: disable=invalid-name
@pytest.fixture
def multiple_characters(db):
    """
    A fixture that creates multiple characters and insert them to the database.
    """
    character_data_all = get_character_data()
    character_objs = []

    for character_data in character_data_all:
        character_obj = Character(**character_data)

        db.session.add(character_obj)

        character_objs.append(character_obj)

    db.session.add_all(character_objs)

    yield character_objs

    # Cleanup - delete the objects from the database
    for character_obj in character_objs:
        db.session.delete(character_obj)


# pylint: disable=invalid-name
@pytest.fixture
def multiple_films(db, multiple_characters):
    """
    A fixture that creates multiple films and insert them to the database.
    """
    film_data_all = get_film_data(multiple_characters)
    film_objs = []

    for film_data in film_data_all:
        table_obj = Film(**film_data)

        db.session.add(table_obj)

        film_objs.append(table_obj)

    db.session.add_all(film_objs)

    yield film_objs

    # Cleanup - delete the objects from the database
    for film_obj in film_objs:
        db.session.delete(film_obj)
