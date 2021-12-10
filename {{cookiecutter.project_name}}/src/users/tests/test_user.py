import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from users.models import User

pytestmark = [pytest.mark.django_db]


def test_username_is_case_insensitive():
    user = User.objects.create(username="test")

    assert user == User.objects.get(username="TEST")


def test_username_is_unique():
    with pytest.raises(IntegrityError) as e:  # noqa: PT012
        User.objects.create(username="test")
        User.objects.create(username="test")

        assert "duplicate" in e.args[0]


def test_username_should_contain_only_ascii():
    with pytest.raises(ValidationError):
        User(username="Иван").full_clean()


def test_email_is_case_insensitive():
    user = User.objects.create(email="test@example.com")

    assert user == User.objects.get(email="TEST@EXAMPLE.COM")


def test_email_is_unique():
    with pytest.raises(IntegrityError) as e:  # noqa: PT012
        User.objects.create(username="test1", email="test@example.com")
        User.objects.create(username="test2", email="test@example.com")

        assert "duplicate" in e.args[0]


def test_email_is_mandatory():
    with pytest.raises(ValidationError) as e:  # noqa: PT012
        User(username="Ivan").full_clean()

        assert e["email"] == ["This field cannot be blank."]
