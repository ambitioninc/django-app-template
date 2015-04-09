# flake8: noqa
from .version import __version__

django_app_config = '{{project_name}}.apps.{{ project_name | replace("_", " ") | title | replace(" ", "") }}Config'
