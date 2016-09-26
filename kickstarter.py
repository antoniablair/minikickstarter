# install sqlite

from cmd import Cmd
from painter import paint

from settings.base import GREETING, ERROR_MSG, SYNTAX_MSG
from projects.actions import *

def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print paint.green(logo)

# Confirm there are enough parameters
def number_args_correct(args, expected_args):
    if args < expected_args:
        print ERROR_MSG
        print paint.red(u'Please use the correct syntax.')
        return False
    else:
        return True



class MiniKickstarterPrompt(Cmd):
    def do_back(self, args):
        """Back a project with the format: back <given name> <project> <credit card number> <backing amount>"""
        project_args = args.split()

        if number_args_correct(len(project_args), 4):
            back_project(*project_args)

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
        """Create a new project using this format: project <project> <targetamount>"""
        project_args = args.split()

        if number_args_correct(len(project_args), 2):
            create_project(project_args)
        # else:
        #     print ERROR_MSG
        #     print paint.red(u'Please use the correct format: project <project> <target amount>')

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
        print SYNTAX_MSG
        prompt.cmdloop(GREETING)
