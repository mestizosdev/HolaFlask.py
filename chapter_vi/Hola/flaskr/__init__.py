# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flaskr.config.database import db
from flaskr.config.logger import define_logger
from flaskr.config.routes import load_routes
from flaskr.seeder import Seeder


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_pyfile('config/config.cfg')
db.init_app(app)

from flaskr.config.models import *  # noqa

migrate = Migrate(app, db)

load_routes(api)
define_logger()


@app.cli.command('seed')
def seed():
    Seeder.seed()


@app.cli.command('unseed')
def undo_seed():
    Seeder.unseed()


app.config['MAIL_SERVER'] = '0.0.0.0'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message(subject='Hello from flask application!', sender='jorge@hola.dev', recipients=['sol@friend.io'])
    msg.body = "Hello Sol, how are you?"
    mail.send(msg)
    return "Message sent!"
