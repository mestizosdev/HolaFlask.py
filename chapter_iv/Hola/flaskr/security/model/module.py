# -*- coding: utf-8 -*-
from flaskr.config.database import db
from sqlalchemy import ForeignKey


class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    observation = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )
    module_id = db.Column(db.Integer, ForeignKey('modules.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    parent = db.relationship('Module', backref='Module', remote_side=id)
    role = db.relationship('Role', backref='Module')

    def __init__(self, name: str, observation: str, parent=None):
        self.name = name
        self.observation = observation
        self.parent = parent
