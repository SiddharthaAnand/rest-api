from flask import Flask, jsonify
from .config import app_config


def create_app(env_name):
    """
    Creation of the flask app based on the environment.
    :param env_name:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])

    # app.register_blueprint(author_blueprint, url_prefix='/api/v1/author')

    @app.route('/', methods=['GET'])
    def say_hello():
        return jsonify({'route': '/', 'answer': 'hello there! I am alive :)'})

    return app
