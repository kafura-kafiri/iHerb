from flask import Blueprint, request, jsonify
from config import brands
from crud import crud
from utility import request_attributes
from pymongo import DESCENDING

blue = Blueprint('brands', __name__)
crud(blue, brands)


@blue.route('/sug/')
def suggest_brands(query, size):
    query = query if query else request_attributes(request, query=str)['query']
    size = size if size else request_attributes(request, size=int)['size']
    __brands = brands.find(
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
    return __brands