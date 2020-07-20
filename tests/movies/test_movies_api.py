"""Test cases for task_data routes."""

import pandas

from server import movies_info
from server.models.film import Film
from server.models.character import Character


# pylint: disable=unused-argument
def test_update_movies_info(flask_client, mock_get_url):
    """
    Testing the UpdateMoviesInfo class to get movies data.

    Here we are using a mock fixture with the redefined method get_url
    of the UpdateMoviesInfo class.
    """

    movies_info.update_movies_info()

    # There should only be one movie in the db with one related character.
    films = Film.query.all()

    assert films
    assert films[0].title == "Castle in the Sky"
    assert films[0].people
    assert len(films[0].people) == 1
    assert films[0].people[0].name == "Colonel Muska"

    # Cleanup
    Character.query.delete()
    Film.query.delete()


def test_movies_table(flask_client, multiple_characters, multiple_films):
    """
    Testing the GET /movies route.

    Should return full movies table. The db now consists of 2 films and
    4 related characters from two fixtures.
    """
    expexted_values = ['My Neighbor Totoro', 'Totoro', 'Chu Totoro',
                       'Chibi Totoro', "Kiki's Delivery Service", 'Jiji']
    response = flask_client.get("/movies")

    assert response.status_code == 200

    html_page = pandas.read_html(response.data)

    # Ensure that we have dataset
    assert html_page

    # The page object is the first item of the dataset
    html_page = html_page[0]

    # We have 4 top level columns - Film id, Title, Release date, People
    assert len(html_page.columns) == 4
    # import pdb; pdb.set_trace()
    # print(html_page.People.to_string())
    # We have 2 films and 4 characters, let's check
    assert len(html_page.Title) == 6

    # And there are exactly values that were set in fixtures
    assert set(html_page.Title) <= set(expexted_values)
