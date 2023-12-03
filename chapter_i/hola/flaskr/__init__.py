from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .logger import define_logger
from .routes import load_routers

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from .models import *  # noqa

migrate = Migrate(app, db)

load_routers(api)
define_logger()
