import os, pickle

# install sqlite

from cmd import Cmd
from painter import paint

from settings.base import GREETING, ERROR_MSG
from projects.actions import *

def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print (paint.green(logo))

class MiniKickstarterPrompt(Cmd):
    def do_hello(self, args):
        """A greeting."""
        # if len(args) == 0:
        #     name = 'stranger'
        # else:
        #     name = args
        # print 'Hello, %s' % name
        print u'Hello yourself!'

    def do_quit(self, args):
        """Quit Mini Kickstarter."""
        print u'Goodbye!'
        raise SystemExit

    def do_project(self, args):
        """Create a new project using this format: project <project> <target amount>"""
        if len(args) == 0:
            print ERROR_MSG
            pass
        else:
            create_project(args)

    def do_projects(self, args):
        """To view a list of projects, type 'projects'."""

        actual_projects = [p for p in PROJECT_LIST if p != '']
        print actual_projects

        if len(actual_projects) < 1:
            print u'There are no current projects.'
        else:
            if len(actual_projects) is 1:
                print u'There is currently 1 project:\n'
            else:
                print u'There are currently {} projects:\n'.format(len(actual_projects))
            for project in actual_projects:
                print project

    def do_list(self, name):
        """View information about a project with: list <projectname>"""

    def do_instructions(self, args):
        """Type instructions to view Mini Kickstarter's commands."""
        print u'Instructions coming soon!'


# Todo: Move these somewhere more legit

# def save(data, LOCAL_DATA):
#     with open(LOCAL_DATA, 'w') as db:
#         db.write(string_from_data(data))
#
# def retrieve(LOCAL_DATA):
#     with open(LOCAL_DATA) as db:
#         return data_from_string(db.read())

# def save(data, filename):
#     with open(filename, 'w') as fh:
#         fh.write(string_from_data(data))


# utility functions? serializer stuff


if __name__ == '__main__':
    prompt = MiniKickstarterPrompt()
    prompt.prompt = '> '

    show_logo()

    try:
        prompt.cmdloop(GREETING)
    except Exception as e:
        # prevents the app from shutting itself down after each error
        print ERROR_MSG
        print u'{}'.format(e)
        print paint.red(u'\nMaybe you made a typo? Please try again.\n')
        prompt.cmdloop(GREETING)
