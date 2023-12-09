# -*- coding: utf-8 -*-
from flask import current_app as app
from flaskr.config.database import db
from ..model.user import User


class UserService:
    @staticmethod
    def find_all():
        users = User.query.all()

        users_dict = [
            {'id': user.id, 'username': user.username} for user in users
        ]

        return users_dict

    @staticmethod
    def find_by_id(id):
        user = User.query.filter_by(id=id).first()

        if user:
            user_dict = {'id': user.id, 'username': user.username}

            return user_dict

        return None

    @staticmethod
    def save(data):
        try:
            user = User(username=data['username'], password=data['password'])
            db.session.add(user)
            db.session.commit()

            user_dict = {'id': user.id, 'username': user.username}

            return user_dict
        except Exception as e:
            app.logger.error(f'Error to save user: {e}.')
            raise ValueError('Error to save user.')

    @staticmethod
    def update(id, data):
        try:
            user = User.query.filter_by(id=id).first()

            if user:
                user.username = data['username']
                user.password = data['password']

                db.session.commit()

                user_dict = {'id': user.id, 'username': user.username}

                return user_dict

            return None
        except Exception as e:
            app.logger.error(f'Error to update user: {e}.')
            raise ValueError('Error to update user.')

    @staticmethod
    def delete(id):
        try:
            user = User.query.filter_by(id=id).first()

            if user:
                db.session.delete(user)
                db.session.commit()

                return True

            return False
        except Exception as e:
            app.logger.error(f'Error to delete user: {e}.')
            raise ValueError('Error to delete user.')
