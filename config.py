# $Id$
# Copyright (c) 2021 pocketservices GmbH

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # MongoDB Atlas
    MONGO_URI = 'mongodb+srv://watch:w741.-gs@diary.vgtmh.mongodb.net/main' + \
        '?retryWrites=true&w=majority'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    # cookie security
    SESSION_COOKIE_SECURE    = True
    REMEMBER_COOKIE_SECURE   = True
    REMEMBER_COOKIE_HTTPONLY = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development' : DevelopmentConfig,
    'production'  : ProductionConfig
}
