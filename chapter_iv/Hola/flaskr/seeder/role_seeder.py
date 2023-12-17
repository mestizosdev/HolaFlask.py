from flaskr.config.database import db
from flaskr.config.models import Role


class RoleSeeder:
    @staticmethod
    def create():
        db.session.add(Role(name='admin'))
        db.session.add(Role(name='user'))
        db.session.commit()

    @staticmethod
    def remove():
        Role.query.delete()
        db.session.commit()
