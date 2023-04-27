import requests


def test_beer_details():
    response = requests.get('https://api.punkapi.com/v2/beers/8')
    assert response.status_code == 200
    data = response.json()[0]
    assert data['name'] == 'Fake Lager'
    assert data['abv'] == 4.7


def test_delete_beer():
    response = requests.delete('https://api.punkapi.com/v2/beers/8')
    assert response.status_code == 404
    assert response.json()['message'] == 'No endpoint found that matches \'/v2/beers/8\''
