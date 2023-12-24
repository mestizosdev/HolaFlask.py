import pytest
from flaskr import create_app, db, Seeder


@pytest.fixture(scope='session')
def flask_app():
    app = create_app('test')
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture(scope='session')
def app_with_db(flask_app):
    db.create_all()
    Seeder.seed()

    yield flask_app

    db.session.commit()
    db.drop_all()
