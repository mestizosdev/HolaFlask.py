# -*- coding: utf-8 -*-
from flask_restful import Resource
import platform
from ..service.version_service import find_version


class VersionController(Resource):
    def get(self):
        return {
            'application': {
                'name': 'HolaFlask.py',
                'author': 'Jorge Luis',
                'version': '1.0.0',
                'versionOS': f'{platform.system()} {platform.release()}',
                'versionDatabase': find_version(),
                'versionPython': platform.python_version(),
            }
        }
