from django.test import TestCase
from django.db.utils import OperationalError
from django.core.management import call_command

from unittest.mock import patch


class DatabaseConnectionTests(TestCase):

    def test_wait_for_db_ready(self):
        """Waiting for DB when DB is available"""

        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:

            gi.return_value = True
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 1)

    @patch("time.sleep", return_value=True)
    def test_wait_for_db(self, ts):
        """Waiting for DB"""

        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 6)
