# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask_mail import Mail, Message
from flask import request, current_app as app
from flask_pydantic import validate
from ..schema.email_schema import RecipientBody


class MailController(Resource):
    @validate(body=RecipientBody)
    def post(self):
        data = request.get_json()
        mail = Mail(app)

        sender = app.config['MAIL_EMAIL']
        name = data['name']
        recipient = data['email']

        msg = Message(
            subject='Hello from HelloFlask.py!',
            sender=sender,
            recipients=[recipient],
        )
        msg.body = f'Hello {name}, how are you?'
        mail.send(msg)

        return {'message': 'Email sent!'}
