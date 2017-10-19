from flask import Blueprint, request, redirect, render_template
from flask_login import login_required, current_user
from crud import request_json
from config import sessions, homes
blue = Blueprint('epay', __name__)
import datetime
from bson import ObjectId
from services import handle


@blue.route('/', methods=['POST', 'GET'])
@login_required
def pay():
    _json = request_json(request)
    _json['user'] = current_user.__dict__
    _json['date'] = datetime.datetime.now()
    _json['home'] = homes.find_one({'_id': ObjectId(_json['home'])})
    _json['_id'] = ObjectId()
    from services import handle
    handle(_json)
    return redirect(_json['redirect'], code=302)


@blue.route('/<_id>', methods=['GET', 'POST'])
def answer(_id):
    session = sessions.find_one({'_id': ObjectId(_id)})
    if request.method == 'GET':
        return '''
                <form action='/services/epay/{}' method='POST'>
                    <input type='checkbox' name='value' id='value' placeholder=''></input>
                    <input type='text' name='text' id='text' placeholder=''></input>
                    <input type='submit' name='submit'></input>
                </form>
                '''.format(_id)
    if request.method == 'POST':
        value = request.values['value']
        text = request.values['text']
        value = 'yes u can \n' if value == 'on' else "no u can't \n"
        session['answer'] = value + text
        handle(session)
        if not value:
            pay_back(session)

def pay_back(session):
    pass