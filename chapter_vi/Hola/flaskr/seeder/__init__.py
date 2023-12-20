import time
from flaskr.seeder.role_seeder import RoleSeeder
from flaskr.seeder.user_seeder import UserSeeder
from flaskr.seeder.module_seeder import ModuleSeeder


class Seeder:
    @staticmethod
    def seed():
        start = time.time()
        RoleSeeder.create()
        UserSeeder.create()
        ModuleSeeder.create()
        end = time.time()
        print(f'{round(end - start, 2)} seconds')

    @staticmethod
    def unseed():
        ModuleSeeder.remove()
        RoleSeeder.remove()
        UserSeeder.remove()
