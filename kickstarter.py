# install sqlite

# argparse

import argparse
import re
from cmd import Cmd
from painter import paint

from projects.actions import *
from backings.actions import *

def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print paint.green(logo)

# Confirm there are enough parameters
def correct_amount_args(args, expected_args):

    if len(args) != expected_args:
        print paint.red(u'{}\nPlease make sure you\'re using the right number of variables.').format(ERROR_MSG)
        return False
    else:
        return True

# Todo: Move these
def remove_dollar_sign(price):
    if type(price) == str:
        if price[0] == '$':
            price = price[1:].replace(",", "")
        return price

def numbers_are_numeric(args, number_indexes):
    """Given the index numbers of certain items in a list, makes sure they are numbers."""
    for number in number_indexes:
        try:
            float(args[number])
        except ValueError:
            return False
    return True

def is_numeric(str):
    """See if string is numeric."""
    try:
        float(str)
    except ValueError:
        return False
    return True

def is_alphanumeric(str):
    if re.match("^[A-Za-z0-9_-]*$", str):
        return True
    else:
        return False

def correct_char_count(str, min, max):
    chars = len(str)
    if min <= chars <= max:
        return True
    else:
        return False

# ----------------------------------

class MiniKickstarterPrompt(Cmd):
    # def do_count(self, args):
    #     args = args.split()
    #     if correct_amount_args(args, 2):
    #         empty = ''
    #         query_db(args[0], args[1], empty, query_all=False, count=True)

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
                # Add and is no longer than 19 chars
                if is_numeric(card) and is_luhn_valid(card):
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
            view_all_from_db('Backings')

    def do_backer(self, name):
        """See what a particular backer has backed with: backer <personname>"""
        # args = args.split()
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
        print u'Instructions coming soon!'

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
            view_all_from_db('Projects')

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
