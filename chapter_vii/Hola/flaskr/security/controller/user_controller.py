# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_pydantic import validate
from flask_jwt_extended import jwt_required, get_jwt
from ..service.user_service import UserService
from ..schema.user_schema import UserBody, UserBodyUpdate


class Users(Resource):
    @jwt_required()
    def get(self):
        jwt = get_jwt()
        roles = jwt.get('roles')

        if 'Manager' in roles or 'Administrator' in roles:
            return jsonify(UserService.find_all())

        return {'message': 'Access forbidden'}, 403


class UserById(Resource):
    @jwt_required()
    def get(self, id):
        user = UserService.find_by_id(id)

        if user:
            return jsonify(user)

        return {'message': 'User not found'}, 404

    @jwt_required()
    @validate(body=UserBodyUpdate)
    def put(self, id):
        """Not update password"""
        try:
            data = request.get_json()
            status, result_dict = UserService.update(id, data)

            if status:
                return jsonify(result_dict)

            return result_dict, 404
        except ValueError as e:
            return {'message': str(e)}, 500

    @jwt_required()
    def delete(self, id):
        try:
            status = UserService.delete(id)

            if status:
                return {'message': 'User deleted'}

            return {'message': 'User not found'}, 404
        except ValueError as e:
            return {'message': str(e)}, 500


class User(Resource):
    @jwt_required()
    @validate(body=UserBody)
    def post(self):
        try:
            data = request.get_json()
            if UserService.find_by_username(data['username']):
                return {'message': 'Username is already registry'}, 404
            else:
                if UserService.find_by_email(data['email']):
                    return {'message': 'Email is already registry'}, 404

            return make_response(jsonify(UserService.save(data)), 201)
        except ValueError as e:
            return {'message': str(e)}, 500
