import sqlite3 as sqlite

from backings.models import Backing
from projects.models import Project
from settings.constants import *
from utils.data import query_db

def update_project(project_name, new_currently_raised):
    """Update a project after it raises more money."""
    try:
        con = sqlite.connect('test.db')
        cur = con.cursor()

        query_string = u'UPDATE Projects SET currently_raised={} WHERE name={}'.format(currently_raised, self.name)

        cur.execute(query_string)

        con.commit()
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

    query_string = u'SELECT * FROM PROJECTS WHERE name=\'{}\''.format(project_name)

    project = query_db(query_string, silent=True, fetch_one=True)

    if project is None or len(project) == None:
        print (LOOKUP_ERROR).format(project_name)
    else:
        query_string=(u'SELECT * FROM BACKINGS WHERE card={} AND project=\'{}\'').format(card, project_name)
        result = query_db(query_string, silent=True)

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


def view_backer(name):
    """View a backer and the projects they have backed."""
    query_string = (u'SELECT * FROM BACKINGS WHERE NAME=\'{n}\';').format(n=name)

    backings = query_db(query_string, silent=True, as_dict=True)

    if len(backings) == 0:
        print (LOOKUP_ERROR).format(name)
    else:
        print u'{} has backed:'.format(name)
        for b in backings:
            print u'- {} for ${}'.format(b["project"], b["amount"])
