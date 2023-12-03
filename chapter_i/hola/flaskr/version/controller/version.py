from flask_restful import Resource
import platform


class Version(Resource):
	def get(self):
		return {
			'application': {
				'name': 'HolaFlask.py',
				'author': 'Jorge Luis',
				'version': '1.0.0',
				'versionOS': f'{platform.system()} {platform.release()}',
				'versionDatabase': 'version.version_database',
				'versionPython': platform.python_version(),
			}
		}
