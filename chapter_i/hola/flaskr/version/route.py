from .controller.version_controller import Version


def define_routers(api):
    api.add_resource(Version, '/hola/v1/version')
