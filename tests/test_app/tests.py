from django.test import TestCase
from django.core.management import call_command
from cStringIO import StringIO


class MigrationTestCase(TestCase):
    def test_has_no_migrations(self):
        buf = StringIO()
        call_command('makemigrations', '--dry-run', stdout=buf)
        buf.seek(0)
        out = buf.getvalue()
        self.assertEqual(out, 'No changes detected\n')
