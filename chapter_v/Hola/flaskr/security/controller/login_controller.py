# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_pydantic import validate
from ..service.login_service import LoginService
from ..schema.user_schema import UserBody


class Register(Resource):
    @validate(body=UserBody)
    def post(self):
        try:
            data = request.get_json()
            return make_response(jsonify(LoginService.register(data)), 201)
        except ValueError as e:
            return {'message': str(e)}, 500
