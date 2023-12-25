# -*- coding: utf-8 -*-
from flask_mail import Mail, Message
from flask import current_app as app


class MailHelper:
    @staticmethod
    def send_mail(name: str, recipient: str, token: str):
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
            f'http://localhost:5000/hola/v1/user/signup/confirm/{token}'
        )
        mail.send(msg)

        return {'message': 'Email sent!'}
