from ast import literal_eval
from bson import ObjectId


def request_json(request, _json=None, specific_type=dict):
    raw = None
    if _json:
        raw = _json
    elif 'json' in request.values:
        raw = request.values['json']
    else:
        raise Exception
    try:
        evaluated = literal_eval(raw)
        if specific_type and type(evaluated) is specific_type:
            return evaluated
        elif not specific_type:
            return evaluated
        else:
            raise Exception
    except Exception as e:
        return raw


def request_attributes(request, **kwargs):
    values = request.values
    _json = {}
    for kay, _type in kwargs.items():
        if kay not in values:
            raise AttributeError()
        else:
            value = values[kay]
            if _type is str:
                evaluated_value = value
            else:
                evaluated_value = literal_eval(value)
                if type(evaluated_value) is not _type:
                    raise TypeError()
            _json[kay] = evaluated_value
    return _json


def obj2str(tree):
    if isinstance(tree, dict):
        for k, node in tree.items():
            tree[k] = obj2str(node)
        return tree
    elif isinstance(tree, list):
        _tree = []
        for node in tree:
            _tree.append(obj2str(node))
        return _tree
    elif isinstance(tree, ObjectId):
        return str(tree)
    else:
        return tree


def str2obj(tree):
    if isinstance(tree, dict):
        for k, node in tree.items():
            tree[k] = str2obj(node)
        return tree
    elif isinstance(tree, list):
        _tree = []
        for node in tree:
            _tree.append(str2obj(node))
        return _tree
    try:
        return ObjectId(tree)
    except:
        return tree


def free_from_(tree):
    if isinstance(tree, dict):
        new_tree = {}
        for k, node in tree.items():
            if '__' not in k:
                new_tree[k] = free_from_(node)
        return new_tree
    elif isinstance(tree, list):
        for idx, node in enumerate(tree):
            tree[idx] = free_from_(node)
    return tree