from telethon import TelegramClient
from telethon.tl.types import UpdateShortChatMessage, UpdateShortMessage
from config import homes, users, sessions
from bson import ObjectId

api_id = 165248
api_hash = '287208e1887c8e18f37d92a545a26376'
phone = '+989133657623'


def load_tg():
    client = TelegramClient('/home/pouriya/PycharmProjects/SheyRoon/services/tg/always_logged', api_id, api_hash)
    client.connect()

    # client.sign_in(phone=phone)
    # client.sign_in(code=25178)

    '''def sprint(string, *args, **kwargs):
        """Safe Print (handle UnicodeEncodeErrors on some terminals)"""
        try:
            print(string, *args, **kwargs)
        except UnicodeEncodeError:
            string = string.encode('utf-8', errors='ignore')\
                           .decode('ascii', errors='ignore')
            print(string, *args, **kwargs)'''

    """def update_handler(update_object):
        import json
        print(update_object)
        if isinstance(update_object, UpdateShortMessage):
            if update_object.out:
                sprint('You sent {} to user #{}'.format(
                    update_object.message, update_object.user_id))
            if not update_object.out:
                '''if session[update_object.user_id]:
                    _session = session[update_object.user_id]
                    _session['answer'] = update_object.message
                    _session['_id'] = str(_session['_id']) # <<<<<<<<<< important TODO
                    print(json.dumps(_session, indent=2))
                    from services import handle
                    handle(_session)'''
                sprint('[User #{} sent {}]'.format(update_object.user_id, update_object.message))

        if isinstance(update_object, UpdateShortChatMessage):
            if update_object.out:
                sprint('You sent {} to chat #{}'.format(
                    update_object.message, update_object.chat_id))
            else:
                sprint('[Chat #{}, user #{} sent {}]'.format(
                    update_object.chat_id, update_object.from_id,
                    update_object.message))

    client.add_update_handler(update_handler)"""

    from services import passer

    @passer()
    def send_earnest_request_to_hosts(_json):
        from flask import current_app
        domain = current_app.config['domain']
        if _json['action'] == 'earnest' and 'answer' not in _json:
            user_first_name = _json['user']['first_name']
            home_title = _json['home']['title']
            phones = [host['phone'] for host in _json['home']['hosts']]
            phones = set(phones)
            for phone in phones:
                client.send_message(phone, "(mister|miss) {} want's your home ({})".format(user_first_name, home_title))
                client.send_message(phone, "do you accept or decline click below")
                client.send_message(phone, domain + 'services/epay/' + str(_json['_id']))

    @passer()
    def receive_earnest_request_from_hosts(_json): # u may notif more than one because of amo of hosts
        print('im here tg')
        if _json['action'] == 'earnest' and 'answer' in _json:
            answer = _json['answer']
            client.send_message(_json['user']['phone'], answer)

"""
    import telethon.tl.functions as tl
    import telethon.tl.types as types


    def get_user_id(phone_number):
        '''
        try:
            return client._get_entry()
        except:
            others
        :param phone_number:
        :return:
        '''
        contact = types.InputPhoneContact(client_id=0, phone=phone_number, first_name=phone_number[1:], last_name="")
        result = client(tl.contacts.ImportContactsRequest([contact]))
        try:
            #  client(tl.contacts.DeleteContactsRequest([contact]))
            imported = result.__dict__['imported'][0]
            return imported.user_id
        except:
            class UserNotFound(Exception):
                pass
            raise UserNotFound()"""