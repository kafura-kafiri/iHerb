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
    from crud._services.analytics import show_trending
    context['products'] = show_trending()
    return render_template('homepage/index.html', **context)

from views import search