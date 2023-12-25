# -*- coding: utf-8 -*-
from flask import current_app as app
from typing import Tuple
from flaskr.config.database import db
from flaskr.utils.password import encrypt
from ..model.user import User


class UserService:
    @staticmethod
    def find_all():
        users = User.query.all()

        users_dict = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }
            for user in users
        ]

        return users_dict

    @staticmethod
    def find_by_id(id):
        user = User.query.filter_by(id=id).first()

        if user:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }

            return user_dict

        return None

    @staticmethod
    def save(data):
        try:
            user = User(
                username=data['username'],
                email=data['email'],
                password=encrypt(data['password']),
            )
            db.session.add(user)
            db.session.commit()

            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }

            return user_dict
        except Exception as e:
            app.logger.error(f'Error to save user: {e}')
            raise ValueError('Error to save user')

    @staticmethod
    def update(id, data) -> Tuple[bool, dict]:
        try:
            user = User.query.filter_by(id=id).first()

            if user:
                if data['username'] != user.username:
                    if (
                        User.query.filter_by(username=data['username']).count()
                        > 0
                    ):
                        return False, {'message': 'Username is already registry'}

                if data['email'] != user.email:
                    if User.query.filter_by(email=data['email']).count() > 0:
                        return False, {'message': 'Email is already registry'}

                user.username = data['username']
                user.email = data['email']
                user.status = data['status']

                db.session.commit()

                user_dict = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'status': user.status,
                }
                return True, user_dict

            return False, {'message': 'User not found'}
        except Exception as e:
            app.logger.error(f'Error to update user: {e}')
            raise ValueError('Error to update user')

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
            app.logger.error(f'Error to delete user: {e}')
            raise ValueError('Error to delete user')

    @staticmethod
    def find_by_username(username):
        user = User.query.filter_by(username=username).first()

        if user:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }

            return user_dict

        return None

    @staticmethod
    def find_by_email(email):
        user = User.query.filter_by(email=email).first()

        if user:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }

            return user_dict

        return None

    @staticmethod
    def find_status_password_by_username(username) -> Tuple[bool, str]:
        user = User.query.filter_by(username=username).first()

        if user:
            return user.status, user.password

        return False, ''
