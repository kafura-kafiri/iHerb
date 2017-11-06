from flask import Blueprint, request, render_template
from config import hows
from crud import crud
from crud.how.instance import how
from bson import ObjectId
from media import insert_img
blue = Blueprint('how', __name__, template_folder='templates')
crud(blue, hows, template='how/index', load_document=lambda x: (x, {}), skeleton=how)


@blue.route('/<_id>/<level_1>/<level_2>/media/+', methods=['POST'])
def add_image(_id, level_1, level_2):
    (l1, l2) = (int(level_1) - 1, int(level_2) - 1)
    article = hows.find_one({'_id': ObjectId(_id)})
    level_1 = article['level_1'][l1]
    level_2 = level_1['level_2'][l2]
    raw_img = request.files['image']
    o = ObjectId()
    o = insert_img(raw_img.read(), o, sizes=())
    level_2['i'] = str(o[0])
    hows.update(
        {"_id": article['_id']},
        article,
        upsert=True
    )
    return o


@blue.route('/')
def hows_homepage():
    return render_template('how/homepage/index.html')