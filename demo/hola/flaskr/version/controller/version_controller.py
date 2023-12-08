from flask_restful import Resource
import platform
from ..service.version_service import get_version


class Version(Resource):
    def get(self):
        return {
            'application': {
                'name': 'HolaFlask.py',
                'author': 'Jorge Luis',
                'version': '1.0.0',
                'versionOS': f'{platform.system()} {platform.release()}',
                'versionDatabase': get_version(),
                'versionPython': platform.python_version(),
            }
        }
