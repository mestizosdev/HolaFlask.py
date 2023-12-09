# -*- coding: utf-8 -*-
from .controller.ping_controller import PingController


def define_routes(api):
    api.prefix = '/hola/v1'
    api.add_resource(PingController, '/ping')
