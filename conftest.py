import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, ProfileFactory, EnquiryFactory

register(UserFactory)
register(ProfileFactory)
register(EnquiryFactory)


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


@pytest.fixture
def profile(db, profile_factory):
    profile = profile_factory.create()
    return profile


@pytest.fixture
def enquiry(db, enquiry_factory):
    enquiry = enquiry_factory.create()
    return enquiry
