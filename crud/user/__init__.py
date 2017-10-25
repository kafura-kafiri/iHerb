from flask import Blueprint, render_template
from config import users
from crud import crud
from utility import obj2str
from flask_login import login_required, current_user


def load_user(user):
    from config import products, hows
    wish_list = user['wish_list']
    _pr = wish_list['products']
    _pr = products.find({"_id": {"$in": _pr}})
    _hows = wish_list['hows']
    _hows = hows.find({'_id': {"$in": _hows}})

    context = {
        'products': [obj2str(_home) for _home in _pr],
        'hows': [obj2str(_home) for _home in _hows],
    }
    return user, context


blue = Blueprint('users', __name__,template_folder='templates')
crud(blue, users, template='user/index', load_document=load_user)


@blue.route('/me')
@login_required
def profile():
    return render_template('user/profile.html')


@blue.route('/me/wishlist')
@login_required
def wish_list():
    return render_template('user/wishlist.html')


@blue.route('/me/messages')
def messages():
    return render_template('user/messagecenter.html')