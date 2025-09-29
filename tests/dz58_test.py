import pytest
from dz58 import is_email_unique

@pytest.fixture
def users_fixture():
    return [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Eve", "email": "alice@example.com"},
    ]

def test_is_email_unique_true(users_fixture):
    assert is_email_unique(users_fixture, "bob@example.com") is True

def test_is_email_unique_false(users_fixture):
    assert is_email_unique(users_fixture, "alice@example.com") is False

def test_is_email_unique_empty_list():
    assert is_email_unique([], "any@example.com") is False

def test_is_email_unique_no_matching_email(users_fixture):
    assert is_email_unique(users_fixture, "nonexistent@example.com") is False

def test_is_email_unique_email_missing(users_fixture):
    users_with_missing_email = users_fixture + [{"name": "MissingEmail"}]
    assert is_email_unique(users_with_missing_email, "bob@example.com") is True