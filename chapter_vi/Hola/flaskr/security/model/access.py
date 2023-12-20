# -*- coding: utf-8 -*-
from flaskr.config.database import db


class Access(db.Model):
    __tablename__ = 'access'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    read = db.Column(db.Boolean, nullable=False, default=False)
    write = db.Column(db.Boolean, nullable=False, default=False)
    update = db.Column(db.Boolean, nullable=False, default=False)
    delete = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    status = db.Column(db.Boolean, nullable=False, default=True)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )

    user = db.relationship('User', backref='Access')
    module = db.relationship('Module', backref='Access')
