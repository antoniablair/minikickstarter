import os, pickle

# install sqlite

from cmd import Cmd
from painter import paint


def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print (paint.green(logo))

ERROR_MSG = paint.red(u'\nOh dear! That doesn\'t look right.\n')
LOCAL_DATA = 'mini_db.txt'

GREETING = u'Welcome to Mini Kickstarter!\n' \
           u'{}\n\nTo create a project, ' \
           u'type "project <projectname> <targetamount>"\nTo see ' \
           u'instructions, type "instructions"\n' \
           u'For help, type "help"'.format('_'*28)

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

    def do_instructions(self, args):
        """Type instructions to view Mini Kickstarter's commands."""
        print u'Instructions coming soon!'


def create_project(args):
    project_args = args.split()
    target = project_args[-1]

    # Users may give their project multiple names
    final_word = len(project_args)-1
    name = ' '.join([str(x) for x in project_args[:final_word]])

    print u'Creating a new project named {} with a target price of {}'.format(name, target)




class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target

    def save(self):
        print u'Saving'
        try:
            with open(LOCAL_DATA, 'w') as db:
                db.write(string_from_data(self.name))
        except:
            print u'that did not work'


# def string_from_data(data):
#     return '\n'.join(data)
#
# def data_from_string(s):
#     return s.split('\n')
#
#

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
def retrieve(filename):
    with open(filename) as fh:
        return data_from_string(fh.read())

def string_from_data(data):
    return '\n'.join(data)

def data_from_string(s):
    return s.split('\n')


if __name__ == '__main__':
    prompt = MiniKickstarterPrompt()
    prompt.prompt = '> '

    if os.path.isfile(LOCAL_DATA):
        PROJECT_LIST = retrieve(LOCAL_DATA)
    else:
        PROJECT_LIST = []

    show_logo()
    
    try:
        prompt.cmdloop(GREETING)
    except Exception as e:
        # prevents the app from shutting itself down after each error
        print ERROR_MSG
        print u'{}'.format(e)
        print paint.red(u'\nMaybe you made a typo? Please try again.\n')
        prompt.cmdloop(GREETING)
