from flask_login import LoginManager, login_required, UserMixin, current_user, login_user, logout_user
from flask import redirect, request, url_for, Blueprint, render_template
from config import users
from hashlib import sha256

skeleton = {
    'wish_list': {
        'products': {},
        'hows': [],
    },
    'notifications': [],
    'page': {
        'title': '',
        'rank': 0,
        'img': '',
        'description': ''
    },
    'name': '',
    'phone': ''
}


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
            user.is_authenticated = sha256(request.form['password'].encode()).hexdigest() == user['password']
            return user
        except:
            return

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            _redirect, _redirect_url, ctx = '', '', {}
            if 'redirect' in request.values:
                _redirect = request.values['redirect']
                ctx['redirect'] = _redirect
                _redirect = "<input type='hidden' name='redirect' id='redirect' value='{}'></input>".format(_redirect)
            elif 'prev_url' in request.values or 'next' in request.values:
                try: _redirect_url = request.values['prev_url']
                except: _redirect_url = request.values['next']
                ctx['prev_url'] = _redirect_url
                _redirect_url = "<input type='hidden' name='prev_url' id='prev_url' value='{}'></input>".format(_redirect_url)

            return render_template('user/login.html', **ctx)

            '''
                   <form action='login' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'></input>
                    <input type='password' name='password' id='password' placeholder='password'></input>
                    <input type='submit' name='submit'></input>
                    {redirect}{redirect_url}
                   </form>
                   '''.format(redirect=_redirect, redirect_url=_redirect_url)
        username = request.form['username']
        json = users.find_one({'username': username})
        if sha256(request.form['password'].encode()).hexdigest() == json['password']:
            user = User(json)
            login_user(user)
            if 'redirect' in request.form:
                _redirect =request.form['redirect']
                return redirect(url_for(_redirect))
            elif 'prev_url' in request.form:
                return redirect(request.form['prev_url'])
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
            _redirect, _redirect_url, ctx = '', '', {}
            if 'redirect' in request.values:
                _redirect = request.values['redirect']
                ctx['redirect'] = _redirect
                _redirect = "<input type='hidden' name='redirect' id='redirect' value='{}'></input>".format(_redirect)
            elif 'prev_url' in request.values or 'next' in request.values:
                try:
                    _redirect_url = request.values['prev_url']
                except:
                    _redirect_url = request.values['next']
                ctx['prev_url'] = _redirect_url
                _redirect_url = "<input type='hidden' name='prev_url' id='prev_url' value='{}'></input>".format(
                    _redirect_url)

            return render_template('user/login.html', **ctx)

            '''
                   <form action='login' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'></input>
                    <input type='password' name='password' id='password' placeholder='password'></input>
                    <input type='submit' name='submit'></input>
                    {redirect}{redirect_url}
                   </form>
                   '''.format(redirect=_redirect, redirect_url=_redirect_url)

        username = request.form['email']
        email = request.form['email']
        password = sha256(request.form['password'].encode()).hexdigest()
        json = {
            'username': username,
            'password': password,
            'email': email,
            **skeleton,
        }
        users.insert_one(json)
        user = User(json)
        login_user(user)
        if 'redirect' in request.form:
            _redirect =request.form['redirect']
            return redirect(url_for(_redirect))
        if 'prev_url' in request.form:
            return redirect(request.form['prev_url'])
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
        elif 'prev_url' in request.values:
            _redirect_url = request.values['prev_url']
            return redirect(_redirect_url)
        else:
            return username
