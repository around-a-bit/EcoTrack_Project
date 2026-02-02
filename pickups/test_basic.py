import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(username="testuser", password="testpass")
    assert user.username == "testuser"
