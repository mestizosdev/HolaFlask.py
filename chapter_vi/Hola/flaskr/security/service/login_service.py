# -*- coding: utf-8 -*-
from flask import current_app as app
from flaskr.config.database import db
from flaskr.utils.password import encrypt
from ..model.user import User


class LoginService:
    @staticmethod
    def signup(data):
        try:
            user = User(
                username=data['username'],
                email=data['email'],
                password=encrypt(data['password']),
            )
            db.session.add(user)
            db.session.commit()

            user_dict = {
                'username': user.username,
                'email': user.email,
                'status': user.status,
            }

            return user_dict
        except Exception as e:
            app.logger.error(f'Error to signup user: {e}')
            raise ValueError('Error to signup user')
