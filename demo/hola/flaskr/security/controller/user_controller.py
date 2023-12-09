    from flask_restful import Resource
from flask import request
from ..service.user_service import UserService


class Users(Resource):
    def get(self):
        return UserService.find_all()


class UserById(Resource):
    def get(self, id):
        user = UserService.find_by_id(id)
        if user is None:
            return {'message': 'User not found'}, 404
        return user

    def put(self, id):
        user = UserService.find_by_id(id)
        if user is None:
            return {'message': 'User not found'}, 404
        data = request.get_json()
        return UserService.update(id, data)

    def delete(self, id):
        user = UserService.find_by_id(id)
        if user is None:
            return {'message': 'User not found'}, 404
        return UserService.delete(id)


class User(Resource):
    def post(self):
        try:
            data = request.get_json()
            return UserService.save(data)
        except ValueError as e:
            return {'message': str(e)}, 500
