from models import Project
from settings.base import PROJECT_LIST

def create_project(args):
    project_args = args.split()
    target = project_args[-1]

    # In case user gives their project multiple names
    final_word = len(project_args)-1
    name = ' '.join([str(x) for x in project_args[:final_word]])

    print u'Creating a new project named {} with a target price of {}'.format(name, target)
    new_project = Project(name, target)

    # Todo: Put in proper format
    PROJECT_LIST.append(new_project)
    print PROJECT_LIST

def list_project(name):
    # Todo: Eliminate this from happening
    projects = [p for p in PROJECT_LIST if p != '']

    for p in projects:
        if p.name == name:
            print u'{} has a target price of {}. It has not yet been backed.'.format(p.name, p.target)