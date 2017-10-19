from flask import Blueprint, request
from flask_login import current_user, login_required
from config import homes
from bson import ObjectId

blue = Blueprint('homes', __name__, template_folder='../templates')

from config import db

collection = db['HOMES']

from crud import crud

skeleton = {
    'location': {
        'place': '',
        'lat': 0,
        'lng': 0,
    },
    'title': '',
    'about': {
        'summary': '',
        'specifications': {

        }
    },
    'specifications': {

    }
}
crud(blueprint=blue, collection=collection, skeleton=skeleton, template='home/index')


@blue.route('/<_id>/reviews/', methods=['GET', 'POST'])
@login_required
def reviews(_id):
    home_id = ObjectId(_id)
    user_id = current_user.json['_id']
    from utility import request_json
    json = request_json(request)
    if 'score' in json:
        review(home_id, message(json), json['score'])
    elif 'reply' in json:
        reply_id = ObjectId(json['reply'])
        reply(home_id, reply_id, message(json))
    else:
        ask(home_id, message(json))
    if 'like' in json:
        like(home_id, user_id, json)
    return 'true'


def reply(home_id, reply_id, _message):
    collection.update_one({'_id': home_id}, {'$add': {'reviews.comments': _message}})
    # parrent.[].append(child)


def ask(home_id, _message):
    # monkeratie
    pass


def review(home_id, _message, score):
    user_id = current_user._id;
    _home = homes.find_one({'_id': home_id})
    guests = _home.guests;
    if user_id in guests:
        avg = _home.reviews.score.avg
        score = avg * _home.reviews.score.size + score;
        _home.reviews.score.size += 1
        _home.reviews.score.avg = score / _home.reviews.score.size;
        _home.reviews.comments.append(_message)
        collection.save(_home)


def message(json):
    import datetime
    now = datetime.datetime.now()

    _message = {
        '_id': '',
        'text': {
            'all': json['text']
        },
        'date': {
            'year': now.year,
            'month': now.month,
            'day': now.day,
        },
        'author': current_user.__dict__,
    }
    if 'score' in json:
        _message['score'] = json['score']

    return _message


def like(home_id, user_id, json):
    from config import users
    if json['like']:
        collection.update_one({'_id': home_id}, {'$addToSet': {'reviews.likes.all': user_id}})
        users.update_one({'_id': user_id}, {'$addToSet': {'wish_list': home_id}})
    if not json['like']:
        collection.update_one({'_id': home_id}, {'$pull': {'reviews.likes.all': user_id}})
        users.update_one({'_id': user_id}, {'$pull': {'wish_list': home_id}})
