from config import analytics
from flask import Blueprint, request, jsonify
from flask_login import current_user
from functools import wraps
from datetime import datetime
from bson import ObjectId
from utility import obj2str
import importlib


def analyze(func):
    @wraps(func)
    def inner(*args,**kwargs):
        response = func(*args, **kwargs)
        print(type(response))
        if isinstance(response, str):
            try:
                collection, action = str(request.url_rule).split('/<_id>')
                collection = collection[1:]
                document = str(request.path)[len(collection) + 2:len(collection) + 2 + 24]
                _analyze(collection, document, action)
            except: pass
            return response
        else:
            return response
    return inner

analytic_order = 0


def _analyze(collection, document, action):
    global analytic_order
    _document = {
        'collection': collection,
        'document': ObjectId(document),
        'action': action,
        'date': datetime.now(),
        'order': analytic_order
    }
    if current_user.is_authenticated:
        _document['user'] = current_user._id
    analytics.insert_one(_document)
    analytic_order += 1


def crud():
    blue = Blueprint('analytics', __name__,template_folder='templates')
    from crud import crud
    crud(blue, analytics)

    jump_back = 5 - 1

    @blue.route('/live/', methods=['GET', 'POST'])
    @blue.route('/live/<int:limit>', methods=['GET', 'POST'])
    @blue.route('/live/<int:limit>/<int:skip>', methods=['GET', 'POST'])
    def live(limit=5, skip=None):
        if not skip:
            skip = analytic_order - jump_back
            skip = 5
        documents = analytics.find({'order': {"$gte": skip, "$lt": skip + limit}})
        documents = [obj2str(document) for document in documents]
        _documents = {}
        for document in documents:
            if document['collection'] not in _documents:
                _documents[document['collection']] = []
            _documents[document['collection']].append(ObjectId(document['document']))
        for _collection, _ids in _documents.items():
            from importlib import import_module
            mod = import_module('config')
            collection = getattr(mod, _collection)
            _documents[_collection] = collection.find({'_id': {"$in": _ids}})
            _documents[_collection] = [obj2str(document) for document in _documents[_collection]]
        _list = []
        for collection_name, collection_set in _documents.items():
            _list.extend(collection_set)
        _list = {
            'list': _list,
            'analytic_order': skip + limit
        }
        return jsonify(_list)
    return blue