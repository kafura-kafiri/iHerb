from flask import Blueprint
from config import users
from crud import crud
from utility import obj2str


def load_user(user):
    from config import homes
    wish_list = user['wish_list']
    _homes = []
    for _id in wish_list:
        _homes.append(homes.find_one({'_id': _id}))
    context = {
        'homes': [obj2str(_home) for _home in _homes],
        #  'place': _place,
        'map_template': 'search'
    }
    return user, context

blue = Blueprint('users', __name__,template_folder='../templates')
crud(blue, users, template='user/page', load_document=load_user)
