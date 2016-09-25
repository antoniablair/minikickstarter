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
        print u'Hello yourself!'

    def do_list(self, name):
        """View information about a project with: list <projectname>"""
        list_project(name)

    def do_instructions(self, args):
        """Type instructions to view Mini Kickstarter's commands."""
        print u'Instructions coming soon!'

    def do_project(self, args):
        """Create a new project using this format: project <project> <target amount>"""
        if len(args) == 0:
            print ERROR_MSG
            pass
        else:
            create_project(args)

    def do_projects(self, args):
        """To view a list of projects, type 'projects'."""
        view_all_projects()

    def do_quit(self, args):
        """Quit Mini Kickstarter."""
        print u'Goodbye!'
        raise SystemExit

# Starts up the app
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
