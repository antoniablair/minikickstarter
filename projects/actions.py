from backings.actions import *
from painter import paint

from projects.models import Project
from settings.constants import DASHED_LINE, ERROR_MSG, LOOKUP_ERROR
from utils.data import query_db


def create_project(name, target):
    if find_existing(name, 'Projects'):
        print ERROR_MSG
        print u'This project already exists. Please try a different name.'
    else:
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        new_project = Project(name, target)
        new_project.save()
#         todo: Sanitize data


def get_number_backers(name):

    try:
        qs = ('SELECT count(*) FROM Backings WHERE project=?')
        args = (name,)
        result = query_db(qs, args=args, silent=False, fetch_one=True)

        if result is not None:
            number_backers = result[0]
        else:
            number_backers = 0
    except:
        number_backers = 0

    return number_backers


def find_existing(name, table):
    """Determines if project or backer exists already"""

    if table == 'Projects':
        qs = 'SELECT * FROM PROJECTS WHERE name=?'

    else:
        qs = 'SELECT * FROM BACKINGS WHERE project=?'

    args = (name, )
    result = query_db(qs, args=args, silent=True)

    try:
        if table == 'Backings':
            return result
        else:
            return True
    except KeyError:
        return None


def list_project(name):
    """Retrieve a project from db and display information about its funding status."""

    qs = ('SELECT * FROM projects WHERE name=?')
    args = (name, )

    row = query_db(qs, args=args, silent=False, fetch_one=True)

    if row != None:
        name = row['name']
        target = row['target']
        currently_raised = row['currently_raised']

        if target > currently_raised:
            amount_needed = target - currently_raised
        else:
            amount_needed = 0

        number_backers = get_number_backers(name)
        backers = find_existing(name, 'Backings')
        s = 's'

        if number_backers == 1:
            s = ''

        print u'{} has a target goal of ${}. It has {} backer{} and ' \
              u'has currently raised ${}.'.format(name, target, number_backers, s, currently_raised)

        if amount_needed != 0:
            print u'\nThis project needs ${} more to be successful!'.format(amount_needed)
        else:
            print paint.green(u'\nThis project has reached its funding goal!')

        if backers != None:
            print u'Backers\n{}'.format(DASHED_LINE)

            for b in backers:
                print u'{} backed {} with ${}'.format(b['name'], name, b['amount'])

    else:
        print paint.red(LOOKUP_ERROR).format(name)


def display_all_results(name, results):
    if len(results) < 1:
        print u'\nThere are no current {}s. We\'re counting on you!'.format(name)
    else:
        if len(results) is 1:
            print u'\nThere is currently 1 project:\n'
        else:
            print u'\nThere are currently {} {}:\n{}\n'.format(len(results), name, DASHED_LINE)
        for result in results:

            if name == 'projects':
                print u'{} - Raised ${} of a ${} goal'.format(result['name'], result['currently_raised'], result['target'])
            else:
                print u'{} backed {} with ${}'.format(result['name'], result['project'], result['amount'])



