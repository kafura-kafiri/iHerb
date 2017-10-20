from flask import Blueprint, request, jsonify
from config import products
from crud import crud
from utility import request_attributes
from crud.pr.instance import ctx, pr

blue = Blueprint('pr', __name__, template_folder='templates')
crud(blue, products, template='pr/index', load_document=lambda x: ({'pr': x}, ctx), skeleton=pr)