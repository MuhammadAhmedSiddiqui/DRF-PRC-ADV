from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestAdminPages(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.admin_user = get_user_model().objects.create_superuser(
            email="ahmed.siddiqui@gmail.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="ahmed.siddiqui@test.com",
            password="password123",
            name="Ahmed Siddiqui"
        )

    def test_users_list_in_admin(self):
        url = reverse("admin:core_user_changelist")

        resp = self.client.get(url)

        self.assertContains(resp, self.user.email)
        self.assertContains(resp, self.user.name)

    def test_users_change_in_admin(self):
        url = reverse("admin:core_user_change", args=(self.user.id, ))

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_users_add_in_admin(self):
        url = reverse("admin:core_user_add")

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
