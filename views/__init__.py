from flask import Blueprint
blue = Blueprint('views', __name__,template_folder='templates')

from views import blue
from flask import render_template, request
from utility import request_attributes, obj2str
from bson import ObjectId

context = {
    'redirect': 'views.homepage',
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
    'products': [
        {
            '_id': '1',
            'title': '1',
            'value': {
                'our': 100,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },  {
            '_id': '2',
            'title': '2',
            'value': {
                'our': 200,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },  {
            '_id': '3',
            'title': '3',
            'value': {
                'our': 300,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },  {
            '_id': '4',
            'title': '4',
            'value': {
                'our': 400,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },  {
            '_id': '5',
            'title': '5',
            'value': {
                'our': 500,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },  {
            '_id': '6',
            'title': '6',
            'value': {
                'our': 600,
            },  # ractive converts to price
            'reviews': {
                'score': {
                    'value': 4.5,
                    'population': 833,
                }
            },
            'img': ['https://www.images-iherb.com/r/NWY-10700-6.jpg'],
        },
    ],
}


@blue.route('/')
def homepage():
    return render_template('homepage/index.html', **context)


@blue.route('/inspect')
def inspect():
    return render_template('homepage/inspect.html')

import views.search