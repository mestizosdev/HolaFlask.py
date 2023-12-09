# -*- coding: utf-8 -*-
from flaskr.config.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
