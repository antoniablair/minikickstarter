import os, sys
from painter import paint

ERROR_MSG = paint.red(u'\nOh dear! That doesn\'t look right.\n')

LOCAL_DATA = 'mini_db.txt'
PROJECT_LIST = []
BACKING_LIST = []
DASHED_LINE = ('_' * 32)

SYNTAX_MSG = paint.red(u'\nError: Please check your syntax.\n')
LOOKUP_ERROR = paint.red(u'Error: I can\'t find anything for {}.')

WELCOME = u'Welcome to Mini Kickstarter!'.encode('utf8')
HEART = paint.magenta((u'\u2665').encode('utf8'))
QUICKSTART = u'\n{}\n\nTo view projects, type \'projects\'\n' \
             u'To create a project, ' \
             u'type "project <projectname> <targetamount>"\nTo see ' \
             u'instructions, type "instructions"\n' \
             u'For help, type "help"'.format(DASHED_LINE).encode('utf8')

INSTRUCTIONS = u"""Welcome to Mini Kickstarter.\n{}\nTo see all projects,'
             u'type 'projects'. 'To create a project, ' \
             u'type "project <projectname> <targetamount>"\nTo lookup ' \
             u'a project, type 'project <projectname>"\n' \
             u'For help, type "help"'""".format(DASHED_LINE)

GREETING = ' '.join([HEART, WELCOME, HEART, QUICKSTART])
