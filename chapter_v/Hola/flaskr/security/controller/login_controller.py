# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify
from pydantic import BaseModel, EmailStr, constr
from flask_pydantic import validate
from ..service.login_service import LoginService


class UserBody(BaseModel):
    username: str
    email: EmailStr
    password: constr(
        min_length=9,
        max_length=18,
    )


class Register(Resource):
    @validate()
    def post(self, body: UserBody):
        try:
            print(body.password)
            data = request.get_json()
            return jsonify(LoginService.register(data))
        except ValueError as e:
            return {'message': str(e)}, 500
