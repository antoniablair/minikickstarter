import os
from utils.utils import retrieve
from painter import paint

ERROR_MSG = paint.red(u'\nOh dear! That doesn\'t look right.\n')

LOCAL_DATA = 'mini_db.txt'
PROJECT_LIST = []
BACKING_LIST = []
DASHED_LINE = ('_' * 32)

if os.path.isfile(LOCAL_DATA):
    if retrieve(LOCAL_DATA) != ['']:
        PROJECT_LIST = retrieve(LOCAL_DATA)

SYNTAX_MSG = paint.red(u'\nError: Please check your syntax.\n')

WELCOME = u'Welcome to Mini Kickstarter!'.encode('utf8')
HEART = paint.magenta((u'\u2665').encode('utf8'))
QUICKSTART = u'\n{}\n\nTo create a project, ' \
             u'type "project <projectname> <targetamount>"\nTo see ' \
             u'instructions, type "instructions"\n' \
             u'For help, type "help"'.format(DASHED_LINE).encode('utf8')

GREETING = ' '.join([HEART, WELCOME, HEART, QUICKSTART])

