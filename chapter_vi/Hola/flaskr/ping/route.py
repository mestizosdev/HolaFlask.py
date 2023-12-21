# -*- coding: utf-8 -*-
from .controller.ping_controller import PingController
from .controller.mail_controller import MailController


def define_routes(api):
    api.prefix = '/hola/v1'
    api.add_resource(PingController, '/ping')
    api.add_resource(MailController, '/ping/mail')
