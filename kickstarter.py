import re
from cmd import Cmd
from painter import paint

from projects.actions import *
from backings.actions import *
from utils.cleaning import *
from utils.luhn import *

def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print paint.green(logo)


class MiniKickstarterPrompt(Cmd):

    def do_back(self, args):
        """Back a project with the format: back <given name> <project> <credit card number> <backing amount>"""
        args = args.split()
        if correct_amount_args(args, 4):
            backer = args[0]
            project = args[1]
            card = args[2]
            price = args[3]

            price = remove_dollar_sign(price)

            if is_alphanumeric(backer) and correct_char_count(backer, 4, 20):
                if is_numeric(card) and is_luhn_valid(card) and correct_char_count(card, 0, 19):
                    if is_numeric(price):
                        card = int(card)
                        price = float(price)

                        back_project(backer, project, card, price)
                    else:
                        print SYNTAX_MSG
                        print u'Please check your price.'
                else:
                    print SYNTAX_MSG
                    print u'Please enter a correct credit card number.'
            else:
                print SYNTAX_MSG
                print u'Please check the name of your backer for formatting.'

    def do_backings(self, args):
        """View the total backings in the database."""
        args = args.split()

        if correct_amount_args(args, 0):
            results = query_db('SELECT * FROM BACKINGS')
            display_all_results('backings', results)

    def do_backer(self, name):
        """See what a particular backer has backed with: backer <personname>"""
        if is_alphanumeric(name):
            # Todo: sanitize
            view_backer(name)
        else:
            print SYNTAX_MSG

    def do_hello(self, args):
        """A greeting."""
        print u'Hello yourself!'

    def do_instructions(self, args):
        """Type 'instructions' to view Mini Kickstarter's commands."""
        print INSTRUCTIONS

    def do_joke(self, args):
        """A joke."""
        print u'{}\n'.format(JOKE_Q)
        print JOKE_A

    def do_list(self, name):
        """View information about a project with: list <projectname>"""
        if name == '':
            print paint.red(u'Error: Try list <projectname> to view a project.')
        else:
            list_project(name)

    def do_project(self, args):
        """Create a new project using this format: project <project> <targetamount>"""
        args = args.split()

        if correct_amount_args(args, 2):
            project = args[0]
            target = remove_dollar_sign(args[-1])

            if is_alphanumeric(project) and is_numeric(target) and correct_char_count(project, 4, 20):
                target = float(target)
                target = round(target, 2)
                create_project(project, target)
            else:
                # todo: Make these errors more verbose
                print SYNTAX_MSG

    def do_projects(self, args):
        """To view a list of projects, type 'projects'."""
        if correct_amount_args(args, 0):
            results = query_db('SELECT * FROM PROJECTS')
            display_all_results('projects', results)

    def do_quit(self, args):
        """Quit Mini Kickstarter."""
        print u'Goodbye!'
        raise SystemExit

# Starts up the app
if __name__ == '__main__':
    prompt = MiniKickstarterPrompt()
    prompt.prompt = '> '

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if not path in sys.path:
        sys.path.insert(1, path)
    del path

    show_logo()

    try:
        prompt.cmdloop(GREETING)
    except Exception as e:
        # prevents the app from shutting itself down after each error
        print ERROR_MSG
        print u'{}'.format(e)
        print SYNTAX_MSG
        prompt.cmdloop(GREETING)
