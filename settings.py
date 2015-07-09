import os

from django.conf import settings


def configure_settings():
    """
    Configures settings for manage.py and for run_tests.py.
    """
    if not settings.configured:
        # Determine the database settings depending on if a test_db var is set in CI mode or not
        test_db = os.environ.get('DB', None)
        if test_db is None:
            db_config = {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'ambition_dev',
                'USER': 'ambition_dev',
                'PASSWORD': 'ambition_dev',
                'HOST': 'localhost'
            }
        elif test_db == 'postgres':
            db_config = {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'USER': 'postgres',
                'NAME': '{{ project_name }}',
            }
        elif test_db == 'sqlite':
            db_config = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '{{ project_name }}',
            }
        else:
            raise RuntimeError('Unsupported test DB {0}'.format(test_db))

        settings.configure(
            TEST_RUNNER='django_nose.NoseTestSuiteRunner',
            NOSE_ARGS=['--nocapture', '--nologcapture', '--verbosity=1'],
            DATABASES={
                'default': db_config,
            },
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                '{{ project_name }}',
                '{{ project_name }}.tests',
            ),
            ROOT_URLCONF='{{ project_name }}.urls',
            DEBUG=False,
            MIDDLEWARE_CLASSES=(),
            DDF_FILL_NULLABLE_FIELDS=False,
        )
