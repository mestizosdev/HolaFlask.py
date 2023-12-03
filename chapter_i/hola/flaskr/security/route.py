from .controller.user_controller import Users, UserById, User


def define_routers(api):
    api.add_resource(Users, '/hola/v1/users')
    api.add_resource(UserById, '/hola/v1/user/<id>')
    api.add_resource(User, '/hola/v1/user')
