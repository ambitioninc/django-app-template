#!/usr/bin/env python
import argparse
import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


parser = argparse.ArgumentParser(
    description='Python app project setup'
)

parser.add_argument(
    '--author-name', '-a',
    dest='author_name',
    type=str,
    required=True,
    help='Your full name (in quotes)'
)
parser.add_argument(
    '--author-email', '-e',
    dest='author_email',
    type=str,
    required=True,
    help='Your email',
)
parser.add_argument(
    '--pypi-name', '-p',
    dest='pypi_name',
    type=str,
    required=True,
    help='Name for the package on pypi'
)
parser.add_argument(
    '--repo-name', '-r',
    dest='repo_name',
    type=str,
    required=True,
    help='Name of the repository on GitHub'
)
parser.add_argument(
    '--project-name', '-n',
    dest='project_name',
    type=str,
    required=True,
    help='python importable name of the project'
)
parser.add_argument(
    '--rtd-subdomain', '-d',
    dest='rtd_subdomain',
    type=str,
    required=True,
    help='ReadTheDocs subdomain'
)
parser.add_argument(
    '--extension', '-x',
    dest='extensions',
    action='append',
    default=['py', 'rst', 'yml', 'txt', 'cfg', 'coveragerc'],
    required=False,
    help='The file extension(s) to render (default: "py,rst,yml,txt,cfg,coveragerc"). '
         'Use -e multiple times. for multiple extensions'
)


class ProjectSetup(object):
    def __init__(self, args):
        self.args = args

    excluded_files = ['new_project.py']

    def get_context(self):
        """
        Get the context for the templates

        :returns: The template context
        :rtype: dict
        """
        return {
            'pypi_name': self.args.pypi_name,
            'author_name': self.args.author_name,
            'author_email': self.args.author_email,
            'repo_name': self.args.repo_name,
            'project_name': self.args.project_name,
            'rtd_subdomain': self.args.rtd_subdomain,
            'current_year': datetime.utcnow().year,
        }

    def run(self):
        """
        Setup the project
        """
        root_dir = os.getcwd()

        extensions = tuple(self.args.extensions)

        context = self.get_context()

        print 'Rendering files with extensions {0}'.format(
            ', '.join(extensions)
        )

        # Render all files with valid extensions
        for root, dirs, files in os.walk(root_dir):
            for dirname in dirs[:]:
                if dirname.startswith('.') or dirname == '__pycache__':
                    dirs.remove(dirname)
            if '/env' not in root:
                env = Environment(loader=FileSystemLoader(root))

                for filename in files:
                    if filename.endswith(('.pyo', '.pyc', '.py.class')):
                        # Ignore some files as they cause various breakages.
                        continue

                    if filename.endswith(extensions) and filename not in self.excluded_files:
                        template = env.get_template(filename)

                        new_path = '{root}/{filename}'.format(
                            root=root,
                            filename=filename
                        )

                        with open(new_path, 'wb') as new_file:
                            new_file.write(template.render(context))

                        print 'Rendering file {0}'.format(new_path)

        # Rename any files named 'project_name'
        for root, dirs, files in os.walk(root_dir):
            if '/env' not in root:
                for filename in files:
                    if filename.endswith(('.pyo', '.pyc', '.py.class')):
                        # Ignore some files as they cause various breakages.
                        continue

                    if filename.endswith(extensions) and filename not in self.excluded_files:
                        base_filename = filename.split('.')[0]
                        if base_filename in context.keys():

                            extension = filename.split('.')[-1]
                            old_path = '{root}/{filename}'.format(
                                root=root,
                                filename=filename
                            )
                            new_path = '{root}/{filename}.{extension}'.format(
                                root=root,
                                filename=context[base_filename],
                                extension=extension
                            )
                            os.rename(old_path, new_path)
                            print 'Renamed file {0} to {1}.{2}'.format(
                                filename,
                                context[base_filename],
                                extension
                            )

        # Rename any directories named 'project_name'
        for root, dirs, files in os.walk(root_dir):
            if '/env' not in root:
                dirname = root.split('/')[-1]

                if dirname in context.keys():
                    path_parent = '/'.join(root.split('/')[:-1])

                    new_path_name = '{0}/{1}'.format(
                        path_parent,
                        context[dirname]
                    )

                    os.rename(root, new_path_name)
                    print 'Renamed directory {0} to {1}'.format(
                        root,
                        new_path_name
                    )

if __name__ == '__main__':  # pragma: no coverage
    args = parser.parse_args()
    status = ProjectSetup(args)
    status.run()
