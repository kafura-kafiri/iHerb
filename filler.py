from crud.brand.filler import fill as fill_brands
fill_brands()

from crud.category.filler import fill as fill_categories
fill_categories()

from crud.how.filler import fill as fill_hows
fill_hows()

from crud.keyword.filler import fill as fill_keywords
fill_keywords()

from crud.pr.filler import fill as fill_pr
fill_pr()

from crud.user.filler import fill as fill_users
fill_users()

from config import products, categories, brands
_products = products.find()
_products = [product for product in _products]

_categories = categories.find()
_categories = [category for category in _categories]

_brands = brands.find()
_brands = [brand for brand in _brands]

for _product in _products:
    _product['categories'] = _categories[:1]
    _product['brand'] = _brands[0]
    products.save(_product)