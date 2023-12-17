# -*- coding: utf-8 -*-
from flaskr.config.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
