import pickle
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

    if find_project(name):
        print u'\nThis project already exists. Please try a different name.'
    else:
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        new_project = Project(name, target)
        # Todo: Serialize
        pickled_project = pickle.dumps(new_project)

        print pickled_project

        # PROJECT_LIST.append(new_project)

        # Move this
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM projects;")
            cur.execute("INSERT INTO test(project)values(?);", (project, pickled_project))
            con.commit()

        except sqlite.Error, e:

            if con:
                con.rollback()

            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:
            if con:
                con.close()


        # Backers ----------------
#
# def create_backer(name, project, card, amount):
#     backer = Backing(backer_name, project, card, amount)

# make sure this project hasn't been backed by this card before
# def lookup_backer(name):
#     backed_projects = [backer for backer in BACKER_LIST if backer.name == name]
#
#     if len(backed_projects):
#        for each project
#     else:
#         print ERROR_MSG
#         print u'Backer not found: {}\n'.format(name)
#         return None


# ------------------------------


def fetch_project(name):
    project = [p for p in PROJECT_LIST if p.name == name]

    if len(project):
        return project[0]
    else:
        print ERROR_MSG
        print u'Project not found: {}\n'.format(name)
        return None

def find_project(name):
    project = [p for p in PROJECT_LIST if p.name == name]

    if len(project):
        return True
    else:
        return False

def list_project(name):
    """Retrieve a project from db and display information about its funding status."""
    target = None
    currently_raised = 0
    number_backers = 0

    try:
        # todo: Fix all the test.dbs everywhere
        con = sqlite.connect('test.db')
        cur = con.cursor()

        cur.execute("SELECT target, currently_raised FROM projects WHERE name=:name", {"name": name})
        con.commit()
        row = cur.fetchone()

        if row != None:
            target = row[0]
            currently_raised = row[1]

        #     todo: move this to its own special function
            try:
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
