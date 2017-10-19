from bson import ObjectId
from flask import jsonify, render_template, abort, request
from flask_login import login_required, current_user
import json
from utility import request_json, obj2str, free_from_, str2obj


def crud(blueprint, collection, skeleton={}, template='', load_document=lambda x: (x, {})):
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
        collection.delete_one({
            '_id': ObjectId(_id)
        })
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    @blueprint.route('/<_id>-', methods=['GET', 'POST'])
    def minimize(_id):
        try:
            document = collection.find_one({'_id': ObjectId(_id)})
            obj2str(document)
            return jsonify(document)
        except Exception as e:
            return str(e)

    @blueprint.route('/-')
    def minimize_all():
        documents = collection.find()
        documents = [obj2str(document) for document in documents]
        return jsonify(documents)

    @blueprint.route('/<_id>')
    def get(_id):
        try:
            document = collection.find_one({'_id': ObjectId(_id)})
            document, ctx = load_document(document)
        except Exception as e:
            return str(e)
        return render_template(template + '.html', **document, **ctx)

    @blueprint.route('/<_id>$$', methods=['GET', 'POST'])  # when in post post > get beca of $$.html
    #@login_required
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
            document = obj2str(document)
            return render_template('crud/$$.html', **document)
        except Exception as e:
            CSI = "\x1B[%sm"
            print(CSI % '6;30;41' + "sorry I can't update let's bring some thing to show" + CSI % '0')
            try:
                document = collection.find_one({'_id': _id})
                if not document:
                    raise
                document = obj2str(document)
                return render_template('crud/$$.html', ctx=document)
            except Exception as e:
                CSI = "\x1B[%sm"
                print(CSI % '6;30;41' + "sorry I can't show any thing sorry for you" + CSI % '0')
                abort(404)

    @blueprint.route('/<_id>$', methods=['GET', 'POST'])
    #@login_required
    def alter(_id):
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
                        {'$set': {node: _json}},
                        return_document=ReturnDocument.AFTER
                    )
            else:
                _json = request_json(request)
                document = collection.find_one_and_update(
                    {'_id': _id},
                    {'$set': _json},
                    return_document=ReturnDocument.AFTER
                )
            #  document['_id'] = str(document['_id'])
            obj2str(document)
            return render_template(template + '_plus.html', **document)
        except Exception as e:
            print(e)
            try:
                document = collection.find_one({'_id': _id})
                #  document['_id'] = str(document['_id'])
                obj2str(document)
                return render_template(template + '_plus.html', **document)
            except Exception as e:
                print(e)
                abort(405)

    '''@blueprint.route('/')
    def filtrate():
        return '''''
