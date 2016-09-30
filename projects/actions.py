
from backings.actions import *
from painter import paint

from projects.models import Project
from settings.constants import DASHED_LINE, ERROR_MSG, LOOKUP_ERROR
from utils.data import query_db

# Todo: paint.green should be alert

def create_project(name, target):
    if find_project(name):
        print ERROR_MSG
        print u'\nThis project already exists. Please try a different name.'
    else:
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        print target
        print type(target)
        new_project = Project(name, target)
        new_project.save()

        # Todo: new_project.save()

        # Todo: Sanitize data, etc
        # try:
        #     con = sqlite.connect('test.db')
        #     cur = con.cursor()
        #     cur.execute("INSERT INTO projects (name, target, currently_raised)values(?,?,?);", (name, target, 0))
        #     con.commit()
        # except sqlite.Error, e:
        #     if con:
        #         con.rollback()
        #     print "Error %s:" % e.args[0]
        #     sys.exit(1)
        # finally:
        #     if con:
        #         con.close()


def get_number_backers(name):
    number_backers = 0

    try:
        query_string = "SELECT count(*) FROM Backings WHERE project=\'{}\';".format(name)

        result = query_db(query_string, silent=False, fetch_one=True)

        if result is not None:
            try:
                number_backers = result[0]
            except:
                number_backers = 0
    except:
        number_backers = 0

    return number_backers


def find_project(name):
    """Determines if project exists already"""

    qs = 'SELECT * FROM PROJECTS WHERE name=\'{}\''.format(name)

    row = query_db(qs)

    if row:
        return True
    else:
        return False

def find_backers(name):
    """Determines if project exists already"""

    query_string = 'SELECT * FROM BACKINGS WHERE project=\'{}\''.format(name)

    row = query_db(query_string, silent=True, as_dict=True)

    if row:
        return row
    else:
        return None

def list_project(name):
    """Retrieve a project from db and display information about its funding status."""

    qs = 'SELECT * FROM projects WHERE name=\'{}\''.format(name)
    row = query_db(qs, silent=False, as_dict=False, fetch_one=True)

    if row != None:
        name = row[0]
        target = row[1]
        currently_raised = row[2]

        if target > currently_raised:
            amount_needed = target - currently_raised
        else:
            amount_needed = 0

        number_backers = get_number_backers(name)
        backers = find_backers(name)

        print u'{} has a target goal of ${}. It has {} backers and ' \
              u'has currently raised ${}.'.format(name, target, number_backers, currently_raised)

        if amount_needed != 0:
            print u'\nThis project needs ${} more to be successful!'.format(amount_needed)
        else:
            print paint.green(u'\nThis project has reached its funding goal!')

        if backers != None:
            print u'Backers\n{}'.format(DASHED_LINE)

            for b in backers:
                print u'{} backed {} with ${}'.format(b["name"], name, b["amount"])

    else:
        print paint.red(LOOKUP_ERROR).format(name)

def view_all_from_db(table_name):
    table = table_name

    # just removing the s at the end
    # todo: Update to use pluralizing plugin
    name = table_name.rstrip(table_name[-1:]).lower()

    query_string = u'SELECT * FROM {}'.format(table)
    results = query_db(query_string)

    if len(results) < 1:
        print u'\nThere are no current {}s. We\'re counting on you!'.format(name)
    else:
        if len(results) is 1:
            print u'\nThere is currently 1 project:\n'
        else:
            print u'\nThere are currently {} {}s:\n{}\n'.format(len(results), name, DASHED_LINE)
        for result in results:

            # Todo: This is fragile.. Update to query by name of col and not just by index
            if table == 'Projects':
                print u'{} - Raised ${} of a ${} goal'.format(result[0], result[2], result[1])
            else:
                print u'{} backed {} with ${}'.format(result[0], result[1], result[3])
