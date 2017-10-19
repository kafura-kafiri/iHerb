from flask_login import LoginManager, login_required, UserMixin, current_user, login_user, logout_user
from flask import redirect, request, url_for, Blueprint
from config import users


def _hash(x):
    return x


def setup(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    class User(UserMixin):
        def __init__(self, _json):
            self.__dict__ = _json
            self.id = _json['username']

    @login_manager.user_loader
    def user_loader(username):
        try:
            json = users.find_one({'username': username})
            user = User(json)
            return user
        except:
            return

    @login_manager.request_loader
    def request_loader(request):
        username = request.form.get('username')
        try:
            json = users.find_one({'username': username})
            user = User(json)
            user.is_authenticated = _hash(request.form['password']) == user['password']
            return user
        except:
            return

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return '''
                   <form action='login' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'></input>
                    <input type='password' name='password' id='password' placeholder='password'></input>
                    <input type='submit' name='submit'></input>
                   </form>
                   '''

        username = request.form['username']
        json = users.find_one({'username': username})
        if _hash(request.form['password']) == json['password']:
            user = User(json)
            login_user(user)
            if 'redirect' in request.form:
                _redirect =request.form['redirect']
                return redirect(url_for(_redirect))
            else:
                return redirect(url_for('protected'))

        return 'Bad login'

    @app.route('/auto_login')
    def auto_login():
        admin = users.find_one({'username': 'admin'})
        login_user(User(admin))
        return redirect(url_for('protected'))

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return '''
                   <form action='signup' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'></input>
                    <input type='password' name='password' id='pw' placeholder='password'></input>
                    <input type='submit' name='submit'></input>
                   </form>
                   '''

        username = request.form['username']
        password = hash(request.form['password'])
        json = {
            'username': username,
            'password': password,
        }
        users.insert_one(json)
        user = User(json)
        login_user(user)
        if 'redirect' in request.form:
            _redirect =request.form['redirect']
            return redirect(url_for(_redirect))
        else:
            return redirect(url_for('protected'))

    @app.route('/protected')
    @login_required
    def protected():
        return 'Logged in as: ' + current_user.username

    @app.route('/logout')
    @login_required
    def logout():
        username = current_user.username
        logout_user()
        if 'redirect' in request.values:
            _redirect = request.values['redirect']
            return redirect(url_for(_redirect))
        else:
            return username
