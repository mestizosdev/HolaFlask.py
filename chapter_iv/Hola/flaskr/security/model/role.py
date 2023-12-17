# -*- coding: utf-8 -*-
from flaskr.config.database import db


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    create_at = db.Column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )
