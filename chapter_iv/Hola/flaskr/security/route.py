# -*- coding: utf-8 -*-
from .controller.user_controller import User, Users, UserById


def define_routes(api):
    api.prefix = '/hola/v1'
    api.add_resource(User, '/user')
    api.add_resource(Users, '/users')
    api.add_resource(UserById, '/user/<int:id>')
