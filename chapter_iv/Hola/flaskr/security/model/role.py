# -*- coding: utf-8 -*-
from flaskr.config.database import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(
        db.Integer, db.Identity(start=1), primary_key=True
    )
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    status: Mapped[bool] = mapped_column(
        db.Boolean, nullable=False, default=True
    )
    create_at: Mapped[datetime] = mapped_column(
        db.DateTime, nullable=False, server_default=db.func.now()
    )
