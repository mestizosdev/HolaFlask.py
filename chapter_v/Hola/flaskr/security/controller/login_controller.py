# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify, make_response
from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from pydantic_core import PydanticCustomError
from flask_pydantic import validate
from ..service.login_service import LoginService


class UserBody(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('password')
    def check_password(cls, v: str) -> str:
        print('check_password', v)
        if len(v) < 9:
            print('check_password error', v)
            raise PydanticCustomError(
                'value_error',
                'password is too short',
                dict(reason='Not valid password'),
            )
        return v


class Register(Resource):
    @validate(body=UserBody)
    def post(self):
        try:
            data = request.get_json()
            return make_response(jsonify(LoginService.register(data)), 201)
        except ValidationError as e:
            return {'message': str(e)}, 500
        except ValueError as e:
            return {'message': str(e)}, 500
