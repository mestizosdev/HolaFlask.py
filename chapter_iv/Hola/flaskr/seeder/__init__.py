from flaskr.seeder.role_seeder import RoleSeeder


class Seeder:
    @staticmethod
    def seed():
        RoleSeeder.create()

    @staticmethod
    def unseed():
        RoleSeeder.remove()
