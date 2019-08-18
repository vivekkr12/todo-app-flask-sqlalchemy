# version must be updated here, setup.py reads from here
from todoapp.config import Config, TestConfig, ProdConfig

__version__ = '0.0.1'

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

env: str = os.getenv('APP_ENV', None)

app: Flask = Flask(__name__, instance_relative_config=True)
if env is None:
    app.config.from_object(Config())
elif env.lower() == 'test':
    app.config.from_object(TestConfig())
elif env.lower() == 'prod':
    app.config.from_object(ProdConfig())

db: SQLAlchemy = SQLAlchemy(app)
ma: Marshmallow = Marshmallow(app)
