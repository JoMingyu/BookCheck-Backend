from flask_restful import Api
from flasgger import Swagger

from app.docs import TEMPLATE

from app.views.user import *
from app.views.library.book import *
from app.views.library.borrow import *
from app.views.library.library import *


class ViewInjector(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        Swagger(app, template=TEMPLATE)

        api = Api(app)

        api.add_resource(Signup, '/signup')
        api.add_resource(AuthCommonUser, '/auth/common')
        api.add_resource(AuthAdmin, '/auth/admin')
        api.add_resource(Refresh, '/refresh')

        api.add_resource(Book, '/book')
        api.add_resource(Borrow, '/borrow')
        api.add_resource(Library, '/library')
