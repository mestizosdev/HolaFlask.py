# -*- coding: utf-8 -*-
from flask import current_app as app
from flaskr.config.database import db
from flaskr.utils.password import encrypt
from flaskr.utils.token import confirm_token
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

    @staticmethod
    def confirm_email(token: str) -> [bool, dict]:
        try:
            email = confirm_token(token)
        except Exception as e:
            app.logger.error(f'Error to confirm_email: {e}')
            return False, {
                'message': 'The confirmation link is invalid or has expired.'
            }

        user = User.query.filter_by(email=email).first()

        if user:
            if user.status:
                return True, {
                    'message': 'Account already confirmed. Please login'
                }
            else:
                user.status = True
                user.update_at = db.func.now()
                db.session.commit()
                return True, {
                    'message': 'You have confirmed your account. Thanks!'
                }

        return False, {
            'message': 'The confirmation link is invalid or has expired'
        }
