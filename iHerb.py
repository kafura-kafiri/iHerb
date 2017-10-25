from flask import Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'very secret key'
app.config['TESTING'] = True

from trans import trans, update
update()
app.jinja_env.globals.update(_=trans)

from crud.user.login import setup
setup(app)

from media import blue as media
app.register_blueprint(media, url_prefix='/media')

from views import blue as views
app.register_blueprint(views)

from crud.user import blue as user
app.register_blueprint(user, url_prefix='/users')

from crud.pr import blue as pr
app.register_blueprint(pr, url_prefix='/pr')

from crud.how import blue as how
app.register_blueprint(how, url_prefix='/hows')

from crud.keyword import blue as keyword
app.register_blueprint(keyword, url_prefix='/keywords')

from crud.brand import blue as brand
app.register_blueprint(brand, url_prefix='/brands')

from crud.category import blue as category
app.register_blueprint(category, url_prefix='/categories')

from crud._services.order import blue as order
app.register_blueprint(order, url_prefix='/orders')

from crud.review import blue as review
app.register_blueprint(review, url_prefix='/reviews')

from crud._services.analytics import crud as analytic
app.register_blueprint(analytic(), url_prefix='/analytics')

if __name__ == '__main__':
    app.run(port=5000)
