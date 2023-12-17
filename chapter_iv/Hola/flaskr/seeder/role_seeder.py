from flaskr.config.database import db
from flaskr.config.models import Role, UserRole


class RoleSeeder:
    @staticmethod
    def create():
        db.session.add(Role(name='Administrator'))
        db.session.add(Role(name='Manager'))
        db.session.commit()

    @staticmethod
    def remove():
        UserRole.query.delete()
        Role.query.delete()
        db.session.commit()
