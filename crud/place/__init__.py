from flask import Blueprint, request, jsonify
from config import places
from crud import crud
from utility import request_attributes

blue = Blueprint('places', __name__)
crud(blue, places)


@blue.route('/', methods=['GET', 'POST'])
def filtrate():
    _json = request_attributes(request, query=str)
    query = _json['query']
    '''places.find({
        '$text': {
            '$search': query,
            '$language': '',  # what should i do
            '$caseSensitive': False,
            '$diacriticSensitive': False,  # wtf
        }
    })'''
    _places = places.find(
        {'$or':
            [
                {'$text': {'$search': query}}, {'description': {'$regex': query}}
            ]
        }
    )
    list = []
    for _place in _places[:5]:
        _place['_id'] = str(_place['_id'])
        list.append(_place)
    return jsonify(list)
