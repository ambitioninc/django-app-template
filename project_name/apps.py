from django.apps import AppConfig


class {{ project_name | replace("_", " ") | title | replace(" ", "") }}Config(AppConfig):
    name = '{{ project_name }}'
    verbose_name = 'Django {{ project_name | replace("_", " ") | title }}'
