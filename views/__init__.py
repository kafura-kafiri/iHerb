from flask import Blueprint
blue = Blueprint('views', __name__,template_folder='templates')

from views import blue
from flask import render_template, request, render_template_string
from utility import request_attributes, obj2str
from bson import ObjectId
from config import products

context = {
    'banner': [
        {
            'link': "/K-Beauty",
            'img': "https://s.images-iherb.com/cms/banners/dkorebanner1004en-US.jpg",
        }, {
            'link': "/Azelique",
            'img': "https://s.images-iherb.com/cms/banners/dazelbanner1004en-US.jpg",
        }, {
            'link': "/Sports-Oct-Special",
            'img': "https://s.images-iherb.com/cms/banners/dsporbanner1004en-US.jpg",
        }, {
            'link': "/Nutiva",
            'img': "https://s.images-iherb.com/cms/banners/dnutbanner1004en-US.jpg",
        }
    ],
}


@blue.route('/')
def homepage():
    keys = [ObjectId(key) for key in trending.keys()]
    print(keys)
    context['products'] = products.find({'_id': {"$in": keys}})
    return render_template('homepage/index.html', **context)


@blue.route('/trans')
def transitive():
    string = '''
        {{ _('huli') }}
    '''
    return render_template_string(string)


trending = {}
@blue.route('/trending/*')
def clear_trending():
    trending.clear()
    return "['success', 200]", 200
@blue.route('/trending/<_id>+')
def insert_trending(_id):
    trending[_id] = True
    return "['success', 200]", 200
@blue.route('/trending/-')
def show_trending():
    import json
    return json.dumps(trending, indent=2)

import views.search
