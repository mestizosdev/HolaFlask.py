from .controller.ping_controller import Ping


def define_routers(api):
    api.add_resource(Ping, '/hola/v1/ping')
