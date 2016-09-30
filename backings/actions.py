import sqlite3 as sqlite

from .financial import *
from backings.models import Backing
from projects.models import Project
from settings.base import *

from utils.data import query_db, alt_query

# def fetch_project_dict(name):
#     row = None
#
#     try:
#         table = 'Projects'
#         lookup_col = 'name'
#         query_word = name
#
#         con = sqlite.connect('test.db')
#         con.row_factory = sqlite.Row
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Projects")
#
#         rows = cur.fetchall()
#
#         # row = query_db(table, lookup_col, query_word)
#         for row in rows:
#             print row["name"]
#
#     except sqlite.Error, e:
#         if con:
#             con.rollback()
#         row = False
#         print "Error %s:" % e.args[0]
#         sys.exit(1)
#
#     finally:
#         if con:
#             con.close()
#         return row

def update_project(project_name, new_currently_raised):
    print ('inside update')
    try:
        con = sqlite.connect('test.db')
        cur = con.cursor()

        qs = u'UPDATE Projects SET currently_raised={} WHERE name={}'.format(currently_raised, self.name)
        print u'This qs is: '
        print qs

        cur.execute(qs)

        con.commit()
        # row = cur.fetchone()
    except sqlite.Error, e:
        if con:
            con.rollback()
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()


def back_project(backer, project_name, card, price):
    """back <given name> <project> <credit card number> <backing amount>"""
    # project = fetch_project(project_name)

    table = 'Projects'
    lookup_col = 'name'

    con = sqlite.connect('test.db')
    cur = con.cursor()

    project = query_db(table, lookup_col, project_name)


    if project is None:
        print (LOOKUP_ERROR).format(project_name)
    else:


        query_string=(u'SELECT * FROM BACKINGS WHERE card={} AND project=\'{}\'').format(card, project_name)
        result = alt_query(query_string, silent=True)

        if result:
            print paint.red(u'Whoops! This card has already been used to back this project.')
        else:

            new_backing = Backing(backer, project_name, card, price)
            print u'Backing {}...'.format(project_name)

            new_backing.save()

            # Todo: Fix this to use column name queries
            currently_raised = project[2]
            target = project[1]
            new_currently_raised = currently_raised +  price

            project = Project(project_name, target)

            project.update(new_currently_raised)

            print paint.green(u'Success! This project has now raised ${}.'.format(new_currently_raised))

            if new_currently_raised >= target:
                print paint.green(u'Hooray, this project has reached its funding goal!')



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


def view_backer(name):
    con = sqlite.connect('test.db')
    cur = con.cursor()

    backings = None
    con = None

    query_string = (u'SELECT * FROM BACKINGS WHERE NAME=\'{n}\';').format(n=name)

    # Todo: Rename this
    backings = alt_query(query_string, silent=True, as_dict=True)

    if len(backings) == 0:
        print (LOOKUP_ERROR).format(name)
    else:
        print u'{} has backed:'.format(name)
        for b in backings:
            print u'- {} for ${}'.format(b["project"], b["amount"])
