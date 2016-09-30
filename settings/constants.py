import os, sys
from painter import paint

# Todo: Change paint.green to alert and paint.red to error

DASHED_LINE = ('_' * 32)

JOKE_Q = u'What\'s the object-oriented way to become wealthy?'
JOKE_A = u'Inheritance.'

# Messages
ERROR_MSG = paint.red(u'\nOh dear! That doesn\'t look right.\n')
SYNTAX_MSG = paint.red(u'\nError: Please check your syntax.\n')
LOOKUP_ERROR = paint.red(u'Error: I can\'t find anything for {}.')

WELCOME = u'Welcome to Mini Kickstarter!'.encode('utf8')
HEART = paint.magenta((u'\u2665').encode('utf8'))
QUICKSTART = u'\n{}\n\nTo create a project, ' \
             u'type "project <projectname> <targetamount>"\nTo see ' \
             u'instructions, type "instructions"\n' \
             u'For help, type "help"'.format(DASHED_LINE).encode('utf8')

INSTRUCTIONS = u"""
HOW TO USE MINI KICKSTARTER\n{}
To see all projects, type 'projects'.
To create a project, type 'project <projectname> <targetamount>'
To lookup a project, type 'list <projectname>
To back a project, type 'backer <backername> <projectname> <creditcard_number> <amount>'
To view all backings, type 'backings'\n
To run tests, type <nosetests 'kickstarter_tests.py>' in your normal terminal from the tests folder.
For help, type 'help' or 'help <command>'""".format(DASHED_LINE)

GREETING = ' '.join([HEART, WELCOME, HEART, QUICKSTART])
