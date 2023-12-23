import pytest
from flaskr import app, db
from colorama import Fore, init

init()


@pytest.fixture(scope='session')
def flask_app():
    print(Fore.RED + f'URI {app.config["SQLALCHEMY_DATABASE_URI"]}')
    app.config.update(
        {
            'SQLALCHEMY_DATABASE_URI': 'postgresql+psycopg://hola:h@localhost/test',
        }
    )
    print(Fore.CYAN + f'URI {app.config["SQLALCHEMY_DATABASE_URI"]}')

    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture(scope='session')
def app_with_db(flask_app):
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()
