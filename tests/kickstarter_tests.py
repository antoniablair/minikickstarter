
from nose.tools import *
from kickstarter import MiniKickstarterPrompt
from painter import paint
from random import randint
from settings.constants import *

from cStringIO import StringIO
# import sys

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

def setup():
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_hello(prompt)
    assert_in(output[0], u'Hello yourself!')
#
def test_create_existing_project():
    """Cannot create a project that already exists"""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_project('Robot_200 20')
    output = '\n'.join(map(str, output))
    assert_in(u'This project already exists', output)

def test_create_project():
    """Creating a project works."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_project('Random_'+str((randint(0,9)))+' 5')
    output = '\n'.join(map(str, output))
    assert_in(u'Creating a new', output)

def test_for_too_many_arguments():
    """Projects can't be created with the wrong number of parameters."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_project('My Little Pony 3000 $200')
    output = '\n'.join(map(str, output))
    assert_in(u'Oh dear!', output)

def test_list_project():
    """Check that project lists correctly"""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_list('Mystery_Theater')
    assert_in(u'Mystery_Theater has a target goal of', output[0])

def test_list_error_msg():
    """Shows error message if you query a project that does not exist."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_list('Banana_2')
    assert_in(u'Error', output[0])

def back_project_error():
    """Backing a project does not work with error in credit card."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_back('Jane Banana 5512631313 50')
    assert_in(u'Error', output[0])

def back_project():
    """Backing a project works."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_back('Jane My_Project 5555555555554444 50')
    assert_in(u'Success!', output[0])

def view_backer():
    """Viewing a backer works."""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        first_prompt = prompt.do_backer('Jane')
    assert_in(u'Banana for $50.0', output[0])

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"