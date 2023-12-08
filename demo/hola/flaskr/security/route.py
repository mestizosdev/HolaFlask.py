from .controller.user_controller import Users, UserById, User


def define_routers(api):
    api.prefix = '/hola/v1'
    api.add_resource(Users, '/users')
    api.add_resource(UserById, '/user/<id>')
    api.add_resource(User, '/user')
