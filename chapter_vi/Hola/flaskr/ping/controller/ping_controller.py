# -*- coding: utf-8 -*-
from flask_restful import Resource


class PingController(Resource):
    def get(self):
        return {'message': 'pong'}
