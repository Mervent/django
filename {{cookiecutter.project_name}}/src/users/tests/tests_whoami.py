import pytest

pytestmark = [pytest.mark.django_db]


def test_api(api):
    got = api.get("/api/v1/users/self/")

    assert got["id"] == api.user.pk
    assert got["username"] == api.user.username


def test_anonymous_access(api_anon):
    got = api_anon.get("/api/v1/users/self/", as_response=True)

    assert got.status_code == 401
