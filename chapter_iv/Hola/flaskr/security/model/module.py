# -*- coding: utf-8 -*-
from flaskr.config.database import db
from sqlalchemy import ForeignKey


class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    observation = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )
    module_id = db.Column(db.Integer, ForeignKey('modules.id'))
    role_name = db.Column(db.String, db.ForeignKey('roles.name'))

    parent = db.relationship('Module', backref='Module', remote_side=id)
    role = db.relationship('Role', backref='Module')

    def __init__(self, name: str, observation: str, role=None, parent=None):
        self.name = name
        self.observation = observation
        self.role = role
        self.parent = parent
