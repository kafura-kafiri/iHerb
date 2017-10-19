from bson import ObjectId
from flask import render_template, request

from config import products
from utility import request_attributes, obj2str
from views import blue

from crud.keyword import add_keyword, suggest_keywords
from crud.brand import suggest_brands
from crud.category import suggest_categories


@blue.route('/s/')
def search():
    _json = request_attributes(request, query=str, category=str, brand=str, pagesize=int, page=int)
    add_keyword(_json['query'])
    fields = {
        "categories": {
            "$elemMatch": {"title": _json['category']}
        },
        'brand.title': _json['brand'],
    }
    if _json['category'] is None or _json['category'] == '':
        del fields['categories']
    if _json['brand'] is None or _json['brand'] == '':
        del fields['brand.title']
    _products = products.find(
        {
            **fields,
            "$text": {
                "$search": _json['query'],
                "$language": ''
            }
        },
        {"score": {
            "$meta": "textScore"
        }},
    ).sort([(
        "score", {
            "$meta": "textScore"
        }
    )]).skip(
        _json['pagesize'] * (_json['page'] - 1)
    ).limit(
        _json['pagesize']
    )
    _products = [obj2str(_product) for _product in _products]
    ctx = {
        'lang': {
            'dimensions': {
                'currency': '$'
            }
        }
    }
    return render_template('result/index.html', query=_json['query'], products=_products, **ctx)


@blue.route('/sug/')
def suggest():
    kw = request_attributes(request, kw=str)['kw']
    _keywords = suggest_keywords(kw, 5)
    _keywords = [_keyword['title'] for _keyword in _keywords]

    _brands = suggest_brands(kw, 5)
    _brands = [[_brand['title'], str(_brand['_id'])] for _brand in _brands]

    _categories = suggest_categories(kw, 5)
    _categories = [[_category['title'], str(_category['_id'])] for _category in _categories]

    _products = products.find(
        {
            "$text": {
                "$search": kw,
                "$language": ''
            }
        },
        {"score": {
            "$meta": "textScore"
        }},
        {"title": 1}
    ).sort([(
        "score", {
            "$meta": "textScore"
        }
    )]).limit(3)
    _products = [obj2str(_product) for _product in _products]
    return _products

    suggestion = {
        "products": [
            {
                "url": "pr/Nubian-Heritage-African-Black-Soap-Bar-5-oz-141-g/11242",
                "dname": "Nubian Heritage, African Black Soap Bar, 5 oz (141 g)",
                "img": "NBH-10600-13"
            },
            {
                "url": "pr/Madre-Labs-Exfoliating-Soap-Bar-with-Marula-Tamanu-Oils-plus-Shea-Butter-Citrus-5-oz-141-g/68389",
                "dname": "Madre Labs, Exfoliating Soap Bar with Marula & Tamanu Oils plus Shea Butter, Citrus, 5 oz (141 g)",
                "img": "MLI-01044-1"
            },
            {
                "url": "pr/Nubian-Heritage-African-Black-Soap-Body-Wash-Detoxifying-Balancing-13-fl-oz-384-ml/8475",
                "dname": "Nubian Heritage, Body Wash, African Black Soap, Detoxifying & Balancing, 13 fl oz (384 ml)",
                "img": "NBH-10603-3"
            },
            {
                "url": "pr/One-with-Nature-Triple-Milled-Soap-Lavender-Soap-Bar-7-oz-200-g/5779",
                "dname": "One with Nature, Triple Milled Soap, Lavender Soap Bar, 7 oz (200 g)",
                "img": "OWN-00000-8"
            }
        ],
        "categories": _categories,
        "general": _keywords,
        "brands": _brands,
    }
    import json
    suggestion = "iHerbSearchCompletion('{}');".format(json.dumps(suggestion, separators=(',', ':')))
    return suggestion
