.. image:: https://travis-ci.org/ambitioninc/{{ repo_name }}.png
   :target: https://travis-ci.org/ambitioninc/{{ repo_name }}

.. image:: https://coveralls.io/repos/ambitioninc/{{ repo_name }}/badge.png?branch=develop
    :target: https://coveralls.io/r/ambitioninc/{{ repo_name }}?branch=develop

.. image:: https://pypip.in/v/{{ repo_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ repo_name }}/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/{{ repo_name }}/badge.png
    :target: https://pypi.python.org/pypi/{{ repo_name }}/
    :alt: Number of PyPI downloads
{#
{#

Setup Instructions
==================
To start a new project with this template::

    virtualenv env
    . ./env/bin/activate
    pip install jinja2
    python new_project.py --author-name <Your Name> --author-email your.email@ambition.com --pypi-name pypy-package-name --repo-name github-repo-name --project-name python_project_name --rtd-subdomain my-project
    or
    python new_project.py --help


The new_project.py script will create all of the necessary folders and
scaffolding for an app with project_name. Note that while most will name their
projects something like "django-regex-field", the app name is normally a
version of that string without "django" and with underscores instead of dashes.
For example, "regex_field" would be an appropriate project name. Remember to
rename your base folder to be your repo name rather than the project name.

Once the project is copied, it is up to the user to open the setup.py file and
modify the following args:

* description: A short summary of the app. Be sure to write a description, otherwise it will show up as UNKNOWN on pypi.
* keywords: Relevant words associated with your project. Ex: 'api, python, datetime'
* install_requires: Any required packages

Other things to note:

* The .travis.yml file installs all necessary testing requirements, such as
flake8, and coverage. Note that it is required that your repo have 100% code
coverage (including branches)

Adding the project to Github
----------------------------

Go to github.com and:

* Create the initial public repository with nothing (i.e. no README, no LICENSE, etc).
* Put a description.

After the repo has been created, go back to your base folder in your project
and type::

    rm -rf .git # Remove the project template .git folder
    rm new_project.py
    git init
    git add .
    git commit -m 'Project scaffolding'
    git remote add origin git@github.com:ambitioninc/repo-name.git
    git push -u origin master

Please make a "develop" branch of the main project on Github and set "develop"
as the default branch after it has been pushed.

Add Documentation
-----------------

Some project scaffolding documentation has been added for you, but you will
need to add docstrings to your functions, classes, and methods yourself. A
basic example has been added in docs/ref/project_name, but you'll have to
manually tweak that yourself.

Don't forget to add a github webhook to ReadTheDocs so the documentaion is
automatically updated on each build.

Python Versions
---------------

This project automatically has travisci build for python 2.7, and 3.4.d

Register on pypi
----------------

To register the project before you make an initial release, run::

    python setup.py register

#}

{{ repo_name }}
===============

{# Please put your description here #}
I have failed to provide a good README.rst in my project, and you should shun
me if I do any pull requests

Installation
------------
To install the latest release, type::

    pip install {{ pypi_name }}

To install the latest code directly from source, type::

    pip install git+git://github.com/ambitioninc/{{ repo_name }}.git

Documentation
=============

Full documentation is available at http://{{ rtd_subdomain }}.readthedocs.org

License
=======
MIT License (see LICENSE)
