# Supports app creation
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from app.middleware import ErrorHandler, Logger
from app.models import Mongo
from app.views import ViewInjector

cors = CORS()
# To Swagger, or Support AJAX

jwt = JWTManager()
# To JWT Authentication

mail = Mail()
# To send email via SMTP

error_handler = ErrorHandler()
# To handle 4xx, 5xx errors

logger = Logger()
# To log in every context of Flask

db = Mongo()
# To handle MongoDB

view = ViewInjector()
# To Swagger Documentation


def create_app(config_name):
    """
    Creates Flask instance & initialize

    Came from 'Use Application Factory' : http://slides.skien.cc/flask-hacks-and-best-practices/#7

    :rtype: Flask
    """
    app_ = Flask(__name__)
    app_.config.from_pyfile(config_name)

    cors.init_app(app_)
    jwt.init_app(app_)
    mail.init_app(app_)
    error_handler.init_app(app_)
    logger.init_app(app_)
    db.init_app(app_)
    view.init_app(app_)

    return app_

app = create_app('../config/dev.py')
