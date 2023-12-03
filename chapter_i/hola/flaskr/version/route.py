from .controller.version import Version


def define_routers(api):
	api.add_resource(Version, '/hola/v1/version')
