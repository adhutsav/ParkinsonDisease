from flask import Flask
from .BackEnd.server import ser
from .FrontEnd.client import cli

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'newParkisonApp'

    
    #from ..FrontEnd.client import cli
    

    app.register_blueprint(ser, url_prefix='/')
    app.register_blueprint(cli, url_prefix='/')
    return app

