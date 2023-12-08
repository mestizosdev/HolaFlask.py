from .controller.version_controller import Version


def define_routers(api):
    api.prefix = '/hola/v1'
    api.add_resource(Version, '/version')
