
import sys
import sqlite3 as sqlite

from decimal import Decimal
from models import Project
from backings.actions import *
from backings.models import Backing
from painter import paint
from settings.base import DASHED_LINE, BACKING_LIST, PROJECT_LIST, ERROR_MSG, SYNTAX_MSG, LOOKUP_ERROR
from utils.data import query_db

# Todo: paint.green should be alert
# paint.red should be for error


def update_cash_needed(project, price):
    """Remaining cash needed to meet target goal."""
    new_price = float(project.target) - float(price)
    project.target = str(new_price)

def create_project(name, target):
    if find_project(name):
        print ERROR_MSG
        print u'\nThis project already exists. Please try a different name.'
    else:
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        new_project = Project(name, target)

        # Todo: Sanitize data, etc
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            cur.execute("INSERT INTO projects (name, target, currently_raised)values(?,?,?);", (name, target, 0))
            con.commit()
        except sqlite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()


def find_project(name):
    """Determines if project exists already"""

    qs = 'SELECT * FROM PROJECTS WHERE name=\'{}\''.format(name)

    row = alt_query(qs)

    if row:
        return True
    else:
        return False


def get_number_backers(name):
    number_backers = 0

    try:
        query_string = "SELECT count(*) FROM Backings WHERE project=\'{}\';".format(name)

        result = alt_query(query_string, silent=False)

        if result is not None:
            try:
                number_backers = result[0][0]
                print number_backers
            except:
                number_backers = 0
    except:
        number_backers = 0

    return number_backers



def list_project(name):
    """Retrieve a project from db and display information about its funding status."""
    target = None
    currently_raised = 0
    number_backers = 0
    con = 0

    try:
        # todo: Fix all the test.dbs everywhere

        table = 'projects'
        lookup_col = 'name'
        query_word = name

        con = sqlite.connect('test.db')
        cur = con.cursor()

        row = query_db(table, lookup_col, query_word)

        if row != None:
            name = row[0]
            target = row[1]
            currently_raised = row[2]

            if target > currently_raised:
                amount_needed = target - currently_raised
            else:
                amount_needed = 0

        #     todo: move this to its own special function
            number_backers = get_number_backers(name)

            print u'{} has a target goal of ${}. It has {} backers and ' \
                  u'has currently raised ${}.'.format(name, target, number_backers, currently_raised)

            if amount_needed != 0:
                print u'\nThis project needs ${} more to be successful!'.format(amount_needed)
            else:
                print paint.green(u'\nThis project has reached its funding goal!')
        else:
            print paint.red(LOOKUP_ERROR).format(name)
    except sqlite.Error, e:
        if con:
            con.rollback()
        print 'error here'
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()

def view_all_from_db(table_name):
    table = table_name
    empty = ''

    # just removing the s at the end (should actually use a plugin for this)
    name = table_name.rstrip(table_name[-1:]).lower()

    results = query_db(table, empty, empty, query_all=True)

    if len(results) < 1:
        print u'\nThere are no current {}s. We\'re counting on you!'.format(name)
    else:
        if len(results) is 1:
            print u'\nThere is currently 1 project:\n'
        else:
            print u'\nThere are currently {} {}s:\n{}\n'.format(len(results), name, DASHED_LINE)
        for result in results:

            # Todo: This is fragile! Update to query by name of col and not just by index
            if table == 'Projects':
                print u'{} - Raised ${} of a ${} goal'.format(result[0], result[2], result[1])
            else:
                # Todo: Format this
                print u'{} backed {} with ${}'.format(result[0], result[1], result[3])
