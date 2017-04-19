from flask import Flask
from os import urandom

def create_app():
    app = Flask(__name__)
    app.secret_key = urandom(24)

    from config import Conf
    from db import mongo

    app.config.from_object(Conf) #get configuration from config.py
    mongo.init_app(app) 

    #from utils import init_utils, init_errors
    from core import core
    #from admin import admin
    #from auth import auth

    #init_utils(app)
    #init_errors(app)
    app.register_blueprint(core)
    #app.register_blueprint(admin)
    #app.register_blueprint(auth)

    return app

