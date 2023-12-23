# -*- coding: utf-8 -*-
from .controller.user_controller import User, Users, UserById
from .controller.login_controller import Signup, Signin, ConfirmAccount


def define_routes(api):
    api.prefix = '/hola/v1'
    api.add_resource(User, '/user')
    api.add_resource(Users, '/users')
    api.add_resource(UserById, '/user/<int:id>')

    api.add_resource(Signup, '/user/signup')
    api.add_resource(Signin, '/user/signin')
    api.add_resource(ConfirmAccount, '/user/signup/confirm/<string:token>')
