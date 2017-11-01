from bson import ObjectId
from flask import jsonify, render_template, abort, request
from flask_login import login_required, current_user
import json
from utility import request_json, obj2str, free_from_, str2obj
from crud._services.analytics import analyze


def crud(blueprint, collection, skeleton={}, projection=None, template='', load_document=lambda x: (x, {}), redundancies={}):
    """
    :issues modify each method with my custom method

    :param blueprint:
    :param collection:
    :param skeleton:
    :param projection:
    :param template:
    :param load_document:
    :param redundancies:
    :return:
    """
    @blueprint.route('/+', methods=['GET', 'POST'])
    @blueprint.route('/<_id>+', methods=['GET', 'POST'])
    #@login_required
    def create(_id=None):
        try:
            document = request_json(request)
        except:
            from copy import deepcopy
            document = deepcopy(skeleton)
        if _id:
            document['_id'] = ObjectId(_id)
        if current_user.is_authenticated:
            document['_author'] = current_user._id
        if 'insert' in redundancies:
            redundancies['insert'](document)
        result = collection.insert_one(document)
        return obj2str(result.inserted_id)

    @blueprint.route('/*', methods=['GET', 'POST'])
    #@login_required
    def delete_all():
        collection.delete_many({})
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    @blueprint.route('/<_id>*', methods=['GET', 'POST'])
    #@login_required
    def delete(_id):
        if 'delete' in redundancies:
            document = collection.find_one({'_id': ObjectId(_id)})
            redundancies['delete'](document)
        collection.delete_one({
            '_id': ObjectId(_id)
        })
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    @blueprint.route('/<_id>-<dash>', methods=['GET', 'POST'])
    @blueprint.route('/<_id>-', methods=['GET', 'POST'])
    def minimize(_id, dash=''):
        fields = []
        if 'p' in dash and projection:
            fields.append(projection)
        try:
            document = collection.find_one({'_id': ObjectId(_id)}, *fields)
            obj2str(document)
            return jsonify(document)
        except Exception as e:
            return str(e)

    @blueprint.route('/-<dash>')
    @blueprint.route('/-')
    def minimize_all(dash=''):
        fields = []
        if 'p' in dash and projection:
            fields.append(projection)
        documents = collection.find({}, *fields)
        documents = [obj2str(document) for document in documents]
        return jsonify(documents)

    @blueprint.route('/<_id>')
    @analyze
    def get(_id):
        try:
            document = collection.find_one({'_id': ObjectId(_id)})
            document, ctx = load_document(document)
        except Exception as e:
            return str(e), 403
        return render_template(template + '.html', **document, **ctx)

    def universal_alter(_id):
        _id = ObjectId(_id)
        try:
            from pymongo import ReturnDocument
            _json = request_json(request)
            _json = free_from_(_json)
            _json = str2obj(_json)
            document = collection.find_one_and_update(
                {'_id': _id},
                {'$set': _json},
                return_document=ReturnDocument.AFTER
            )
            if 'update' in redundancies:
                redundancies['update'](document)
            document = obj2str(document)
            return render_template('crud/$$.html', **document)
        except Exception as e:
            print("sorry I can't update let's bring some thing to show")
            try:
                document = collection.find_one({'_id': _id})
                if not document:
                    raise
                document = obj2str(document)
            except Exception as e:
                print("sorry I can't show any thing sorry for you")
                abort(404)
            return render_template('crud/$$.html', ctx=document)

    def alter(_id, operator):
        _id = ObjectId(_id)
        try:
            from pymongo import ReturnDocument
            if 'node' in request.values:
                _json = request_json(request, specific_type=None)
                node = request.values['node']
                if not _json:
                    document = collection.find_one_and_update(
                        {'_id': _id},
                        {'$unset': {node: ""}},
                        return_document=ReturnDocument.AFTER
                    )
                else:
                    document = collection.find_one_and_update(
                        {'_id': _id},
                        {'${}'.format(operator): {node: _json}},
                        return_document=ReturnDocument.AFTER
                    )
            else:
                _json = request_json(request)
                document = collection.find_one_and_update(
                    {'_id': _id},
                    {'$set': _json},
                    return_document=ReturnDocument.AFTER
                )
            if 'update' in redundancies:
                redundancies['update'](document)
            if 'ajax' in request.values:
                return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
        except Exception as e:
            print(e)
            try:
                document = collection.find_one({'_id': _id})
            except Exception as e:
                print(e)
                abort(405)
        document, ctx = load_document(document)
        return render_template(template + '_plus.html', **document, **ctx)

    @blueprint.route('/<_id>$', methods=['GET', 'POST'])
    @blueprint.route('/<_id>$<operator>', methods=['GET', 'POST'])
    def alter_wrapper(_id, operator='set'):
        if operator == '$':
            return universal_alter(_id)
        return alter(_id, operator)