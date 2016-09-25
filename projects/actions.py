from models import Project
from painter import paint
from settings.base import PROJECT_LIST, ERROR_MSG

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
        print u'\nCreating a new project named {} with a target price of {}'.format(name, target)
        new_project = Project(name, target, 0)
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
    projects = [p for p in PROJECT_LIST if p.name == name]

    print "Looking up project"

    if len(projects):
        print u'{} has a target price of {}. It has not yet been backed.'.format(projects[0].name, projects[0].target)
    else:
        print paint.green(u'I can\'t find a project named {}, are you sure it exists?').format(name)

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

def back_project(backer, project_name, card, price):
    """back <given name> <project> <credit card number> <backing amount>"""
    # project_args = args.split()
    project = fetch_project(project_name)

    print name
    print price

    if not project is None:
        print "Keeping going bc I found it."
        print "Args: "
        print project

        print u'\n Tonia: Now write some stuff for backing.'