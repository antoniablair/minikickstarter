from decimal import Decimal
from models import Project
from painter import paint
from settings.base import PROJECT_LIST, ERROR_MSG, SYNTAX_MSG

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
    if card.isdigit() and len(card) < 20 and is_luhn_valid(card):
        return True
    return False

def name_is_correct(name):
    if name.isalnum() and 4 <= len(name) <= 20:
        return True
    return False

def remove_symbols(price):
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
# ------------

def back_project(backer, project_name, card, price):
    """back <given name> <project> <credit card number> <backing amount>"""
    project = fetch_project(project_name)
    price = float(remove_symbols(price))
    funds_needed = float(project.funds_needed())

    # # Todo: Move into a check parameters function
    # if project is None or not card_is_correct(card):
    if project is None:
        print paint.red(u'Please enter a correct credit card number.')
    else:
        currently_raised = project.currently_raised + price
        new_funds_needed = funds_needed - price

        # Update project
        project.funds_needed = new_funds_needed
        project.backers[backer] = price
        project.currently_raised = float(currently_raised)
        print paint.green(u'This project has now raised ${}.'.format(currently_raised))
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
        target = remove_symbols(target)
        print u'\nCreating a new project named {} with a target price of ${}.'.format(name, target)
        new_project = Project(name, target)
        # Todo: Serialize
        PROJECT_LIST.append(new_project)

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
        thingy = float(p.funds_needed())
        # Todo: Add grammer plugin
        print u'{} has a target goal of ${}. It has {} backers and ' \
              u'has currently raised ${}.'.format(p.name, p.target, len(p.backers), p.currently_raised)

        print p.currently_raised
        print p.target
        print type(p.currently_raised)
        print type(p.target)
        if float(p.currently_raised) >= float(p.target):
            print paint.green(u'This project has reached its funding target! Hooray!')
        else:
            print u'More funds needed.'
            print u'This project needs ${} to reach its target.'.format(funds_needed)

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
            print u'There are currently {} projects:\n'.format(len(actual_projects))
        for project in projects:
            print project
