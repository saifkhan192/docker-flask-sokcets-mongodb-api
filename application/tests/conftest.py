# from myapp import create_app
import os
import sys

import pytest
from flask import Flask

sys.path.append('/app/application')

from fontend_app import fontend_app


def create_app():
    # create app
    app = Flask("flask_test", root_path=os.path.dirname(__file__))
    app.config["MONGODB_SETTINGS"] = {
        "host": os.environ.get('MONGO_URI'),
        "db": os.environ.get('MONGO_DATABASE')
    }
    app.register_blueprint(fontend_app)
    app.config.from_pyfile('./config.py')
    return app

@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client
