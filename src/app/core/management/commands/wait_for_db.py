from django.db.utils import OperationalError
from django.core.management import BaseCommand
from django.db import connections

import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Command to check for database connections"""

        self.stdout.write("Waiting for database connection...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR("DB unavailable, waiting 1 sec")
                )
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database Connection Established")
        )
