from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("user:create")
CREATE_TOKEN_URL = reverse("user:token")


def get_create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class PublicUserAPITest(TestCase):
    """Test cases for user APIs (Public)"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_user_successfull(self):
        """Test case to create user successfull"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "testpass",
            "name": "Muhammad Ahmed Siddiqui",
        }
        res = self.client.post(path=CREATE_USER_URL, data=payload)
        user = get_user_model().objects.get(**res.data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", res.data)
        self.assertNotIn(user.check_password(payload.get("password")))

    def test_check_user_already_exists(self):
        """Test case to check that user already exists"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "testpass",
            "name": "Muhammad Ahmed Siddiqui",
        }
        get_create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_short_password(self):
        """Test case to check short password length"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "pw",
            "name": "Muhammad Ahmed Siddiqui",
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()

        self.assertFalse(user_exists)

    def test_create_token_successfull(self):
        """Test case to create token successfully"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "testpass",
        }

        get_create_user(**payload)

        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_token_with_invalid_creadentials(self):
        """Test case to create token with invald credentials"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "testpass",
        }

        get_create_user(**payload)

        payload["password"] = "wrong"
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_no_user(self):
        """Test case to create token of user that doesn't exists"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "testpass",
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_missing_fields(self):
        """Test case to create token of wih missing field"""

        payload = {
            "email": "ahmed.siddiqui@gmail.com",
            "password": "",
        }
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
