import pytest
from flaskr import app, db


@pytest.fixture(scope='session')
def flask_app():
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