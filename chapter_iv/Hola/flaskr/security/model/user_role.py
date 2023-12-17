# -*- coding: utf-8 -*-
from flaskr.config.database import db
from sqlalchemy import UniqueConstraint
from flaskr.config.models import User, Role


class UserRole(db.Model):
    __tablename__ = 'user_roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_name = db.Column(db.String, db.ForeignKey('roles.name'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )

    user = db.relationship('User', backref='UserRole')
    role = db.relationship('Role', backref='UserRole')

    UniqueConstraint(user_id, role_name)

    def __init__(self, user: User, role: Role):
        self.user_id = user.id
        self.role_name = role.name
