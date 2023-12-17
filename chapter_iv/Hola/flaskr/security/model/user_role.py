# -*- coding: utf-8 -*-
from flaskr.config.database import db


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )

    user = db.relationship('User', backref='UserRole')
    role = db.relationship('Role', backref='UserRole')

    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id
