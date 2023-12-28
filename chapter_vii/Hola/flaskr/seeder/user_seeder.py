# -*- coding: utf-8 -*-
from flaskr.config.database import db
from flaskr.config.models import User, UserRole, Role
from flaskr.utils.password import encrypt


class UserSeeder:
    @staticmethod
    def create():
        admini = User(
            username='admini',
            email='admini@localhost',
            password=encrypt('123456789Aa@'),
        )
        admini.status = True

        manager = User(
            username='manager',
            email='manager@localhost',
            password=encrypt('123456789Aa@'),
        )
        manager.status = True

        db.session.add(admini)
        db.session.add(manager)
        db.session.add(User('yo', 'yo@localhost', encrypt('123456789Aa@')))

        role_administrator = Role.query.filter_by(name='Administrator').first()
        role_manager = Role.query.filter_by(name='Manager').first()
        db.session.add(UserRole(admini, role_administrator))
        db.session.add(UserRole(manager, role_manager))

        db.session.commit()

    @staticmethod
    def remove():
        User.query.delete()
        db.session.commit()
