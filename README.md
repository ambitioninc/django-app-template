{% if False %}
Installation Instructions
--------

To start a new project with this template:

django-admin.py startproject --template=https://github.com/ambitioninc/django-app-template/zipball/master --extension=py,md,yml project_name

This will create all of the necessary folders and scaffolding for an app with project_name. Note that while most will name their projects something like django-regex-field, the app name is normally a version of that string without "django" and with underscores. For example, regex_field would be an appropriate project name.

Once the project is copied, it is up to the user to open the setup.py file and modify the following args:
- name: The pypi package name and name of the repository (use hyphens rather than underscores)
- description: A short summary of the app
- url: The Ambition Github URL to the repo
- author: Your name
- author_email: Your email

Other things to note:
- CONTRIBTORS is left empty. Add your name to that with your email in parentheses next to it
- You can call python setup.py test and it will install your package and run the one example test included in the template
- The .travis.yml file installs all necessary testing requirements, such as pep8, pyflakes, and coverage. Note that it is required that your repo have 100% code coverage (including branches)

{% endif %}
{{ project_name }}
==================
I have failed to provide a good README.md in my project, and you should shun me if I do any pull requests
