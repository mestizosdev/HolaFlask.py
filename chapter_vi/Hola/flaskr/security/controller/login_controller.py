# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify, make_response, current_app as app
from flask_pydantic import validate
from flask_mail import Mail, Message
from flaskr.utils.token import generate_confirmation_token
from ..service.login_service import LoginService
from ..service.user_service import UserService
from ..schema.user_schema import UserBody


class Signup(Resource):
    @validate(body=UserBody)
    def post(self):
        try:
            data = request.get_json()
            if UserService.find_by_username(data['username']):
                return {'message': 'Username is already registry'}, 404
            else:
                if UserService.find_by_email(data['email']):
                    return {'message': 'Email is already registry'}, 404

            token = generate_confirmation_token(data['email'])
            self.send_mail(data['username'], data['email'], token)

            return make_response(jsonify(LoginService.signup(data)), 201)
        except ValueError as e:
            return {'message': str(e)}, 500

    def send_mail(self, name: str, recipient: str, token: str):
        mail = Mail(app)

        sender = app.config['MAIL_FROM_EMAIL']

        msg = Message(
            subject='Hello from HelloFlask.py!',
            sender=sender,
            recipients=[recipient],
        )
        msg.body = (
            f'Hello {name}, how are you? '
            f'Please confirm your email by clicking on the link: '
            f'http://localhost:5000/confirm/{token}'
        )
        mail.send(msg)

        return {'message': 'Email sent!'}
