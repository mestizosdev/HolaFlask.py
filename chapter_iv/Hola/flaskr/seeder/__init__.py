from flaskr.seeder.role_seeder import RoleSeeder
from flaskr.seeder.user_seeder import UserSeeder


class Seeder:
    @staticmethod
    def seed():
        RoleSeeder.create()
        UserSeeder.create()

    @staticmethod
    def unseed():
        RoleSeeder.remove()
        UserSeeder.remove()
