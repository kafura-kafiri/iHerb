from flask import Blueprint
from config import reviews
from crud import crud
from crud.review.instance import review
from bson import ObjectId
blue = Blueprint('reviews', __name__, template_folder='templates')
crud(blue, reviews, skeleton=review)


def bring_reviews(document, size):
    _reviews = document['reviews']['reviews']
    _reviews = _reviews[:size]
    _top_review = document['reviews']['top_review']
    document['reviews']['reviews'] = reviews.find({'_id': {'$in': _reviews}})
    document['reviews']['top_review'] = reviews.find_one({'_id': _top_review})
    return document


def update_structure():
    pass


def init_structure():
    return {
        'score': {
            'value': 2.9,
            'population': {
                'total': 0,
                '1': 0,
                '2': 0,
                '3': 0,
                '4': 0,
                '5': 0,
            },
        },
        'reviews': [],
        'top_review': '',
    }