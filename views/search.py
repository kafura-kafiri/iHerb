from bson import ObjectId
from flask import render_template, request

from config import products
from utility import request_attributes, obj2str
from views import blue

from crud.keyword import add_keyword, suggest_keywords
from crud.brand import suggest_brands
from crud.category import suggest_categories


def search(kw, size, category=None, brand=None, page=1, auto_completion=True):
    projection = {}

    search_selector = {
        "$or":
            [
                {"$text": {
                    "$search": kw,
                    "$language": ''
                }},
            ],
    }

    if auto_completion:
        search_selector['$or'].append({'title': {'$regex': kw}})

    fields = {
        "categories": {
            "$elemMatch": {"title": category}
        },
        'brand.title': brand,
    }
    if category is None or category == '':
        del fields['categories']
    if brand is None or brand == '':
        del fields['brand.title']
    return products.find(
        {
            **fields,
            **search_selector
        },
        {"score": {
            "$meta": "textScore"
        }},
    ).sort([(
        "score", {
            "$meta": "textScore"
        }
    )]).skip(
        size * (page - 1)
    ).limit(
        size
    )


@blue.route('/s/')
def result():
    _json = request_attributes(request, kw=str, category=str, brand=str, pagesize=int, page=int)
    add_keyword(_json['kw'])
    _products = search(_json['kw'], _json['pagesize'], category=_json['category'], brand=_json['brand'], page=_json['page'], auto_completion=False)
    _products = [obj2str(_product) for _product in _products]
    ctx = {
        'lang': {
            'dimensions': {
                'currency': '$'
            }
        }
    }
    query = {
        'kw': _json['kw'],
        'category': _json['category'],
        'brand': _json['brand'],
        'page': _json['page'],
        'pagesize': _json['pagesize']
    }
    return render_template('result/index.html', query=query, products=_products, **ctx)


@blue.route('/sug/')
def suggest():
    kw = request_attributes(request, kw=str)['kw']
    _keywords = suggest_keywords(kw, 5)
    _keywords = [_keyword['title'] for _keyword in _keywords]

    _brands = suggest_brands(kw, 5)
    _brands = [[_brand['title'], str(_brand['_id'])] for _brand in _brands]

    _categories = suggest_categories(kw, 5)
    _categories = [[_category['title'], str(_category['_id'])] for _category in _categories]

    _products = search(kw, 3)
    _products = [{
        'url': 'pr/' + str(_product['_id']),
        'dname': _product['title'],
        'img': _product['img'][0]
                 } for _product in _products]

    print('products')
    print(_products)

    suggestion = {
        "products": _products,
        "categories": _categories,
        "general": _keywords,
        "brands": _brands,
    }
    import json
    suggestion = "iHerbSearchCompletion('{}');".format(json.dumps(suggestion, separators=(',', ':')))
    return suggestion
