import os
from utils.utils import retrieve
from painter import paint

ERROR_MSG = paint.red(u'\nOh dear! That doesn\'t look right.\n')
LOCAL_DATA = 'mini_db.txt'

GREETING = u'Welcome to Mini Kickstarter!\n' \
           u'{}\n\nTo create a project, ' \
           u'type "project <projectname> <targetamount>"\nTo see ' \
           u'instructions, type "instructions"\n' \
           u'For help, type "help"'.format('_'*28)

PROJECT_LIST = []

if os.path.isfile(LOCAL_DATA):
    if retrieve(LOCAL_DATA) != ['']:
        PROJECT_LIST = retrieve(LOCAL_DATA)