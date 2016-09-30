
import sys
import sqlite3 as sqlite

from decimal import Decimal
from models import Project
from backings.actions import *
from backings.models import Backing
from painter import paint
from settings.base import BACKING_LIST, PROJECT_LIST, ERROR_MSG, SYNTAX_MSG

# Todo: paint.green should be alert
# paint.red should be for error


def update_cash_needed(project, price):
    """Remaining cash needed to meet target goal."""
    new_price = float(project.target) - float(price)
    project.target = str(new_price)

def create_project(name, target):

    # if find_project(name):
    #     print u'\nThis project already exists. Please try a different name.'
    # else:
    print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
    new_project = Project(name, target)
    # Todo: Sanitize data, etc
    # PROJECT_LIST.append(new_project)
    # Move this
    try:
        con = sqlite.connect('test.db')
        cur = con.cursor()
        # cur.execute("SELECT * FROM projects;")
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


def find_row(table, lookup_col, query_word):
    """
    Find rows by a query word and return everything inside it as a string.
    """
    row = None
    con = None

    try:
        # todo: Fix all the test.dbs everywhere
        con = sqlite.connect('test.db')
        cur = con.cursor()

        query_string = u'SELECT * FROM {tn} WHERE {col}=\'{qw}\';'.format(tn=table, col=lookup_col, qw=query_word)
        print u'The query_string is ' + query_string
        cur.execute(query_string)
        row = cur.fetchone()
        # con.commit()
        print u'The row returned is: '
        print row
    except sqlite.Error, e:
        # if con:
        #     con.rollback()
        print u'This is being called'
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()
            return row


def fetch_project(project_name):
    # project = [p for p in PROJECT_LIST if p.name == name]
    table = 'projects'
    lookup_col = 'name'
    query_word = project_name

    row = find_row(table, lookup_col, query_word)
    print row

    if len(project):
        return project[0]
    else:
        print ERROR_MSG
        print u'Project not found: {}\n'.format(name)
        return None

def find_project(name):
    # project = [p for p in PROJECT_LIST if p.name == name]
    table = 'projects'
    lookup_col = 'name'
    query_word = project_name

    row = find_row(table, lookup_col, query_word)
    print row

    if len(project):
        return project[0]
    else:
        print ERROR_MSG
        print u'Project not found: {}\n'.format(name)
        return None


    # if len(project):
    #     return True
    # else:
    #     return False

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

        row = find_row(table, lookup_col, query_word)

        # con = sqlite.connect('test.db')
        # cur = con.cursor()
        #
        # cur.execute("SELECT target, currently_raised FROM projects WHERE name=:name", {"name": name})
        # con.commit()
        # row = cur.fetchone()

        if row != None:
            name = row[0]
            target = row[1]
            currently_raised = row[2]

            print name
            print target
            print currently_raised
        #     todo: move this to its own special function
            try:
                print 'Query backup.'
                con = sqlite.connect('test.db')
                cur = con.cursor()

                cur.execute("SELECT count(*) FROM backings WHERE project=:project", {"project": name})
                con.commit()

                print "Backing info: "
                print cur.fetchone()

                if cur.fetchone() is not None:
                    try:
                        number_backers = cur.fetchall()[0]
                    except:
                        number_backers = 0
            except:
                number_backers = 0

            print u'{} has a target goal of ${}. It has {} backers and ' \
                  u'has currently raised ${}.'.format(name, target, number_backers, currently_raised)

        else:
            print paint.red(u'I can\'t find a project named {}, are you sure it exists?').format(name)
    except sqlite.Error, e:
        if con:
            con.rollback()
        print 'error here'
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()


def view_all_projects():
    projects = [p for p in PROJECT_LIST if p != '']

    if len(projects) < 1:
        print u'There are no current projects. Would you like to start one?'
    else:
        if len(projects) is 1:
            print u'There is currently 1 project:\n'
        else:
            print u'There are currently {} projects:\n'.format(len(projects))
        for project in projects:
            print project
