import pytest


def test_user_str(base_user):
    """Test the custom user model __str__ method."""
    assert base_user.__str__() == f"{base_user.username}"


def test_get_full_name(base_user):
    """Test the custom user model get_full_name method."""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name


def test_get_short_name(base_user):
    """Test the custom user model get_short_name method."""
    assert base_user.get_short_name() == base_user.username
