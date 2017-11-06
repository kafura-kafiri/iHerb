from pymongo import MongoClient
from gridfs import GridFS


def configure(app):
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'very secret key'
    app.config['TESTING'] = True

    from trans import trans, update
    update()
    app.jinja_env.globals.update(_=trans)
    import html
    app.jinja_env.globals.update(unescape=lambda x: html.unescape(x))


client = MongoClient('localhost:27017')
db = client['IHERB']
fs = GridFS(client['IHERB_FS'])


products = db['PRODUCTS']
products.drop_indexes()
products.create_index([("$**", "text")], weights={"$**": 1, "title": 3})
products.create_index([("title", 1)])
pr = products

hows = db['HOWS']
hows.drop_indexes()
hows.create_index([("$**", "text")], weights={"$**": 1, "title": 3})
hows.create_index([("title", 1)])

users = db['USERS']

keywords = db['KEYWORDS']
keywords.drop_indexes()
keywords.create_index([("title", "text")])
keywords.create_index([("title", 1)])

brands = db['BRANDS']
brands.drop_indexes()
brands.create_index([("title", "text")])
brands.create_index([("title", 1)])

categories = db['CATEGORIES']
categories.drop_indexes()
categories.create_index([("title", "text")])
categories.create_index([("title", 1)])

reviews = db['REVIEWS']

orders = db['ORDERS']

analytics = db['ANALYTICS']

sessions = db['SESSIONS']

pages = db['PAGES']
