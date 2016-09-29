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

# Helper functions for money, numbers and credit cards
# todo: move these into another directory

# -----------------------------

def update_cash_needed(project, price):
    """Remaining cash needed to meet target goal."""
    new_price = float(project.target) - float(price)
    project.target = str(new_price)

def create_project(project_args):
    # project_args = args.split()
    target = project_args[-1]

    # In case user gives their project multiple names
    # Todo: This allows users to enter in projects with multiple names, but perhaps it should be deleted
    final_word = len(project_args)-1
    name = ' '.join([str(x) for x in project_args[:final_word]])

    if find_project(name):
        print u'\nThis project already exists. Please try a different name.'
    else:
        target = remove_dollar_sign(target)
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        new_project = Project(name, target)
        # Todo: Serialize
        PROJECT_LIST.append(new_project)

        # Move this
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM projects;")
            cur.execute("INSERT INTO projects (name, target, currently_raised)values(?,?);", (name, target, 0))
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
    # Todo: I Eliminated this empty string project from happening. Can I delete this now??
    # Todo: Just grab the first
    projects = [p for p in PROJECT_LIST if p.name == name]

    con = sqlite.connect('test.db')

    currently_raised = 0
    with con:
        cur = con.cursor()

        cur.execute("SELECT target, currently_raised FROM projects WHERE name=:name", {"name": name})
        con.commit()
        target = cur.fetchone()[0]

        cur.execute("SELECT count(*) FROM backings WHERE project=:project", {"project": name})
        con.commit()
        number_backers = cur.fetchall()[0]
    #     return cursor.fetchone()[0]

    if target:
        # print "Projects are : "
        # print projects
        # print "P is: "
        # print p
        # print type(p)
        # remaining_funds_needed = p.funds_needed()
        # Todo: Add grammer plugin
        # print u'{} has a target of ${}'.format(name, target)
        print u'{} has a target goal of ${}. It has {} backers and ' \
              u'has currently raised ${}.'.format(name, target, number_backers[0], currently_raised)

        # print p.currently_raised
        # print p.target
        # print type(p.currently_raised)
        # print type(p.target)
        if float(currently_raised) >= float(target):
            print paint.green(u'This project has reached its funding target! Hooray!')
        else:
            print u'More funds needed.'
            print u'This project has raised ${} of its target goal of ${}.'.format(currently_raised, target)

        # if len(p.backers) > 0:
        #     print p.backers
    else:
        print paint.red(u'I can\'t find a project named {}, are you sure it exists?').format(name)

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
