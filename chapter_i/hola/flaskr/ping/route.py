from .controller.ping_controller import Ping


def define_routers(api):
    api.prefix = '/hola/v1'
    api.add_resource(Ping, '/ping')
