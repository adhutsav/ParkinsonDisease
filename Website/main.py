from flask import Flask
from FrontEnd.client import cli

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'newParkisonApp'

    app.register_blueprint(cli, url_prefix='/')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
