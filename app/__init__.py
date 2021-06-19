#
# Copyright (c) 2021 Benjamin Lorenz
#

from flask import Flask
from flask_pymongo import PyMongo
from flask.json import JSONEncoder
from bson import ObjectId
from config import config


mongo = PyMongo()

class CustomJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super(CustomJSONEncoder, self).default(o)

def create_app(config_name):
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mongo.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app
