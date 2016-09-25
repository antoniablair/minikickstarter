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
    PROJECT_LIST.append(new_project)