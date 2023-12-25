# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_pydantic import validate
from flask_jwt_extended import create_access_token, create_refresh_token
from flaskr.utils.token import generate_confirmation_token
from flaskr.utils.password import compare
from ..service.login_service import LoginService
from ..service.user_service import UserService
from ..schema.user_schema import UserBody, UserBodyLogin
from ..helper.mail import MailHelper


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

            user = LoginService.signup(data)

            token = generate_confirmation_token(data['email'])
            MailHelper.send_mail(data['username'], data['email'], token)

            return make_response(jsonify(user), 201)
        except ValueError as e:
            return {'message': str(e)}, 500


class ConfirmAccount(Resource):
    def get(self, token):
        try:
            status, message = LoginService.confirm_email(token)
            if status:
                return make_response(jsonify(message), 200)

            return make_response(jsonify(message), 404)
        except ValueError as e:
            return {'message': str(e)}, 500


class Signin(Resource):
    @validate(body=UserBodyLogin)
    def post(self):
        try:
            data = request.get_json()

            (
                status,
                stored_password,
            ) = UserService.find_status_password_by_username(data['username'])

            if status is False and len(stored_password) > 0:
                if compare(data['password'], stored_password):
                    user = UserService.find_by_username(data['username'])
                    token = generate_confirmation_token(user['email'])
                    MailHelper.send_mail(user['username'], user['email'], token)

                    return {'message': 'Account not confirmed'}, 404

            elif status and len(stored_password) > 0:
                if compare(data['password'], stored_password):
                    roles = UserService.find_roles_by_username(data['username'])
                    return jsonify(
                        {
                            'access_token': create_access_token(
                                identity=data['username'],
                                additional_claims={'roles': roles},
                            ),
                            'refresh_token': create_refresh_token(
                                identity=data['username']
                            ),
                        }
                    )

            return {'message': 'Invalid credentials'}, 404
        except ValueError as e:
            return {'message': str(e)}, 500
