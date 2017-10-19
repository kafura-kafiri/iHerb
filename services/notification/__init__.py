from flask import Blueprint, render_template, abort, request
from services import passer
from config import sessions, users
from bson import ObjectId
blue = Blueprint('notification', __name__,template_folder='../../templates')


@blue.route('/')
def index():
    return render_template('notification/index.html')


@blue.route('/<_id>', methods=['GET', 'POST'])
def send_notification(_id, msg=None):
    if not msg:
        try:
            msg = request.values['msg']
        except:
            abort(404)
    users.update_one({'_id': ObjectId(_id)}, {'$push': {'notifications': msg}})
    return 'True'


@blue.route('/<_id>/<index>', methods=['GET', 'POST'])
def delete_notification(_id, index):  # this is not atomic
    try:
        users.update_one({'_id': ObjectId(_id)}, {'$unset': {"notifications.{}".format(index): 1}})
        users.update_one({'_id': ObjectId(_id)}, {'$pull': {"notifications": None}})
        return 'true'
    except:
        return 'false'


@passer()
def send_earnest_request_to_hosts(_json):
    from flask import current_app
    domain = current_app.config['domain']
    if _json['action'] == 'earnest' and 'answer' not in _json:
        user_first_name = _json['user']['first_name']
        home_title = _json['home']['title']
        _ids = [host['_id'] for host in _json['home']['hosts']]
        _ids = set(_ids)
        for _id in _ids:
            send_notification(_id, "(mister|miss) {} want's your home ({}) do you accept or decline click below {}services/epay/{}".format(user_first_name, home_title, domain, str(_json['_id'])))


@passer()
def receive_earnest_request_from_hosts(_json): # u may notif more than one because of amo of hosts
    print("im here notif")
    if _json['action'] == 'earnest' and 'answer' in _json:
        answer = _json['answer']
        _id = _json['user']['_id']
        send_notification(_id, answer)