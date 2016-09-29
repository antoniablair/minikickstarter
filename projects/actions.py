from decimal import Decimal
from models import Project
from backings.models import Backing
from painter import paint
from settings.base import BACKING_LIST, PROJECT_LIST, ERROR_MSG, SYNTAX_MSG

# Todo: paint.green should be alert
# paint.red should be for error

# Helper functions for money, numbers and credit cards
# todo: move these into another directory
def digits_of(number):
    return list(map(int, str(number)))

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def card_is_correct(card):
    # Todo: Removed isdigit, where should this go now
    try:
        if len(str(card)) < 20 and is_luhn_valid(card):
            return True
        return False
    except ValueError:
        return False

def name_is_correct(name):
    if name.isalnum() and 4 <= len(name) <= 20:
        return True
    return False

def remove_dollar_sign(price):
    if type(price) == str:
        if price[0] == '$':
            price = price[1:].replace(",", "")
        return price

def price_is_correct(price):
    # Todo: Work on this
    try:
        float(price)
        return True
    except:
        return False

def convert_to_decimal(str):
    num = Decimal(str)
    return round(num, 2)
# -----------------------------

def back_project(backer, project_name, card, price):
    """back <given name> <project> <credit card number> <backing amount>"""
    project = fetch_project(project_name)

    CARD_ERROR = paint.red(u'Please enter a correct credit card number.')

    # format numbers (move)
    # if project is None or not card_is_correct(card):
    if project is None:
        return

    project.currently_raised = float(project.currently_raised)
    project.target = float(project.target)
    card = float(card)
    price = float(price)

    if float(card).is_integer():
        card = int(card)
    else:
        print CARD_ERROR
        return

    if not card_is_correct(card):
        print CARD_ERROR
        return

    # # Todo: Move into a check parameters function
    else:
        backings = [b for b in BACKING_LIST if b.project == project_name and b.card == card]
        print 'BACKINGS -------'
        print backings
        print BACKING_LIST
        print '//////'
        if len(backings):
            print paint.red(u'This card has already been used to back this project.')
            return

        else:
            new_backing = Backing(backer, project_name, card, price)
            BACKING_LIST.append(new_backing)
            # new_backing.save()
            project.currently_raised = project.currently_raised + price
            # new_funds_needed = funds_needed - price

            # Update project
            # project.funds_needed = new_funds_needed
            # todo: delete this?
            project.backers[backer] = price

            print paint.green(u'This project has now raised ${}.'.format(project.currently_raised))
            print project.target
            print type(project.target)
            if project.currently_raised >= project.target:
                print paint.green(u'Congratulations on reaching your funding goal!')
            # todo: save project here

#     Todo: Finish this

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

    if len(projects):
        p = projects[0]
        # print "Projects are : "
        # print projects
        # print "P is: "
        # print p
        # print type(p)
        # remaining_funds_needed = p.funds_needed()
        # Todo: Add grammer plugin
        print u'{} has a target goal of ${}. It has {} backers and ' \
              u'has currently raised ${}.'.format(p.name, p.target, len(p.backers), p.currently_raised)

        # print p.currently_raised
        # print p.target
        # print type(p.currently_raised)
        # print type(p.target)
        if float(p.currently_raised) >= float(p.target):
            print paint.green(u'This project has reached its funding target! Hooray!')
        else:
            print u'More funds needed.'
            print u'This project has raised ${} of its target goal of ${}.'.format(p.currently_raised, p.target)

        # if len(p.backers) > 0:
        #     print p.backers
    else:
        print paint.red(u'I can\'t find a project named {}, are you sure it exists?').format(name)

def view_all_projects():
    projects = [p for p in PROJECT_LIST if p != '']
    print projects

    if len(projects) < 1:
        print u'There are no current projects.'
    else:
        if len(projects) is 1:
            print u'There is currently 1 project:\n'
        else:
            print u'There are currently {} projects:\n'.format(len(projects))
        for project in projects:
            print project
