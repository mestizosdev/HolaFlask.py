from flaskr.config.database import db
from flaskr.config.models import Module, Role


class ModuleSeeder:
    @staticmethod
    def create():
        main = Module(name='Main', observation='Main')

        role_security = Role.query.filter_by(name='Security').first()
        security = Module(
            name='Security',
            observation='Security management',
            role=role_security,
            parent=main,
        )
        db.session.add(security)
        security_manage = Module(name='Manage', observation='Menu', parent=security)
        db.session.add(
            security_manage
        )
        db.session.add(Module(name='User', observation='Option', parent=security_manage))
        db.session.add(Module(name='Role', observation='Option', parent=security_manage))
        db.session.add(
            Module(name='Transaction', observation='Menu', parent=security)
        )
        db.session.add(
            Module(name='Report', observation='Menu', parent=security)
        )
        db.session.add(
            Module(name='Paremeter', observation='Menu', parent=security)
        )

        role_library = Role.query.filter_by(name='Library').first()
        library = Module(
            name='Library',
            observation='Library management',
            role=role_library,
            parent=main,
        )
        db.session.add(library)
        db.session.add(Module(name='Manage', observation='Menu', parent=library))
        db.session.add(
            Module(name='Transaction', observation='Menu', parent=library)
        )
        db.session.add(Module(name='Report', observation='Menu', parent=library))
        db.session.add(
            Module(name='Paremeter', observation='Menu', parent=library)
        )

        db.session.commit()

    @staticmethod
    def remove():
        Module.query.delete()
        db.session.commit()
