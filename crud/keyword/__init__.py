from flask import Blueprint, request
from config import keywords
from crud import crud
from utility import request_attributes
from pymongo import DESCENDING
from utility import obj2str

blue = Blueprint('keywords', __name__)
crud(blue, keywords)


_keywords = {}
_max_length = 10


def add_keyword(key):
    if key not in _keywords:
        _keywords[key] = 1
    else:
        _keywords[key] += 1
    if len(_keywords) == _max_length:
        for key in _keywords:
            try:
                keywords.update(
                    {"title": key},
                    {"$inc": { "hit": 1 }},
                )
            except:
                keywords.insert_one({
                    "title": key,
                    "hit": 1,
                })
        _keywords.clear()


@blue.route('/sug/')
def suggest_keywords(query, size):
    query = query if query else request_attributes(request, query=str)['query']
    size = size if size else request_attributes(request, size=int)['size']
    __keywords = keywords.find(
        {'$or':
            [
                {'$text': {'$search': query}},
                {'title': {'$regex': query}},
            ]
        }
    ).sort(
        'hit', DESCENDING
    ).limit(
        size
    )
    return __keywords