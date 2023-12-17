# -*- coding: utf-8 -*-
from .controller.version_controller import VersionController


def define_routes(api):
    api.prefix = '/hola/v1'
    api.add_resource(VersionController, '/version')
