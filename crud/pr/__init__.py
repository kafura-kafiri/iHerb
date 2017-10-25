from flask import Blueprint, request, jsonify
from config import products
from crud import crud
from utility import request_attributes
from crud.pr.instance import ctx, pr, projection
from crud.review import bring_reviews

blue = Blueprint('pr', __name__, template_folder='templates')
crud(blue, products, template='pr/index', load_document=lambda x: ({'pr': bring_reviews(x, 5)}, ctx), skeleton=pr, projection=projection)