from flaskr.seeder.role_seeder import RoleSeeder
from flaskr.seeder.user_seeder import UserSeeder
from flaskr.seeder.module_seeder import ModuleSeeder


class Seeder:
    @staticmethod
    def seed():
        RoleSeeder.create()
        UserSeeder.create()
        ModuleSeeder.create()

    @staticmethod
    def unseed():
        ModuleSeeder.remove()
        RoleSeeder.remove()
        UserSeeder.remove()
