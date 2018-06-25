from flask import Flask
from user.ext import init_ext
from user.views import user
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

from user import views,models


def register_blue():
    app.register_blueprint(user,url_prefix='/user')


def create_app():
    init_ext(app=app)
    register_blue()
    return app