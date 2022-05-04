from django.test import TestCase
from django.contrib.auth import get_user_model


class CreateUserTest(TestCase):

    def test_create_user_successfull(self):
        email = "ahmed.siddiqui@gmail.com"
        password = "Testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_user_email(self):
        email = "ahmed.siddiqui@GMAIL.COM"

        user = get_user_model().objects.create_user(
            email=email,
            password="Test123"
        )

        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                password="Test123"
            )

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="ahmed.siddiqui@gmail.com",
            password="Test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
