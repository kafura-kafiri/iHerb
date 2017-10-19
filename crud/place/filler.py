import requests
import json

url = 'http://localhost:5000/places/'

headers = {'content-type': 'application/json'}

places = [
    {
        'lat': 36.7084323,
        'lng': 52.6344572,
        'zoom': 16,
        'country': 'iran',
        'state': 'mazandaran',
        'place': 'بابلسر',
        'score': 9,
    }, {
        'lat': 36.5735855,
        'lng': 52.0147596,
        'zoom': 15,
        'country': 'iran',
        'state': 'mazandaran',
        'place': 'نور',
        'score': 8,
    }, {
        'lat': 36.5735855,
        'lng': 52.0147596,
        'zoom': 15,
        'country': 'iran',
        'state': 'mazandaran',
        'place': 'نمک آبرود',
        'score': 5,
    }, {
        'lat': 36.7084323,
        'lng': 52.6344572,
        'zoom': 16,
        'country': 'iran',
        'state': 'mazandaran',
        'place': 'رامسر',
        'score': 6,
    }, {
        'lat': 36.7084323,
        'lng': 52.6344572,
        'zoom': 16,
        'country': 'iran',
        'state': 'mazandaran',
        'place': 'متل قو',
        'score': 10,
    }
]


def import_places():
    response = requests.post(url + '*')
    print(response.content)

    for place in places:
        place['description'] = '{} {} {}'.format(place['country'], place['state'], place['place'])

    for place in places:
        response = requests.post(url + '+', data={'json': str(place)})
        print(response.content)
