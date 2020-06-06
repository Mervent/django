import pytest
from mixer.backend.django import mixer as _mixer

from app.test.client import APIClient


@pytest.fixture()
def mixer():
    return _mixer


@pytest.fixture
def user(mixer):
    return mixer.blend("users.User")


@pytest.fixture
def api(user):
    return APIClient(user=user)


@pytest.fixture
def api_anon():
    return APIClient()
