from flask import Blueprint, request
from config import hows
from crud import crud
blue = Blueprint('how', __name__, template_folder='templates')
crud(blue, hows, template='how/index', load_document=lambda x: (x, {}))