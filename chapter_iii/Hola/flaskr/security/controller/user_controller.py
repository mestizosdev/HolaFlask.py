# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import request, jsonify
from ..service.user_service import UserService


class Users(Resource):
    def get(self):
        return jsonify(UserService.find_all())


class UserById(Resource):
    def get(self, id):
        user = UserService.find_by_id(id)

        if user:
            return jsonify(user)

        return {'message': 'User not found.'}, 404

    def put(self, id):
        try:
            data = request.get_json()
            user = UserService.update(id, data)

            if user:
                return jsonify(user)

            return {'message': 'User not found.'}, 404
        except ValueError as e:
            return {'message': str(e)}, 500

    def delete(self, id):
        try:
            status = UserService.delete(id)

            if status:
                return {'message': 'User deleted.'}

            return {'message': 'User not found.'}, 404
        except ValueError as e:
            return {'message': str(e)}, 500


class User(Resource):
    def post(self):
        try:
            data = request.get_json()
            return jsonify(UserService.save(data))
        except ValueError as e:
            return {'message': str(e)}, 500
