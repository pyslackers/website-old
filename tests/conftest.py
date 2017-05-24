import pytest

from website import create_app
from website.config import resolve_config
from website.external import db


@pytest.fixture()
def app():
    app_ = create_app(resolve_config('test'))
    with app_.app_context():
        db.create_all()
        yield app_
        db.drop_all()


@pytest.fixture()
def test_client(app):
    yield app.test_client()
