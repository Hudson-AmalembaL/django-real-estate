import pytest


def test_base_user_has_no_username(user_factory):
    """Test that an error is raised when a user with no username is created."""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)

    assert str(err.value) == "Users must submit a username"


def test_base_user_has_no_first_name(user_factory):
    """Test that an error is raised when a user with no first name is created."""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must submit a first name"


def test_base_user_has_no_last_name(user_factory):
    """Test that an error is raised when a user with no last name is created."""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must submit a last name"


def test_super_user_is_not_staff(user_factory):
    """Test that an error is raise when a superuser has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    """Test that an error is raised when a superuser has is_superuser set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superusers must have is_superuser=True"


def test_base_user_email_is_normalized(base_user):
    """Test that the email is normalized"""
    email = "hudson.LUSENO@gMAIL.com"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """Test that an admin users email is normalized"""
    email = "hudson.LUSENO@gMAIL.com"
    assert super_user.email == email.lower()


def test_create_super_user_with_no_email(user_factory):
    """Test that a super user is created with email"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"


def test_create_base_user_with_no_email(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_super_user_with_no_password(user_factory):
    """Test that a super user is created with a password"""
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superusers must have a password"


def test_user_email_incorrect(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email="real.com")
    assert str(err.value) == "YOu must provide a valid email address"
