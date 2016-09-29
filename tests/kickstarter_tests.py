import sys
from nose.tools import *
from kickstarter import MiniKickstarterPrompt
from projects.actions import *

from cStringIO import StringIO
import sys

PROJECT_LIST = []

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
def test_create_project():
    """Check that a basic project creates correctly"""
    prompt = MiniKickstarterPrompt()
    with Capturing() as output:
        prompt.do_project('Robot 200')
    output = '\n'.join(map(str, output))
    assert_in(u'Creating a new project named Robot', output)

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
        prompt.do_list('Banana')
    assert_in(u'I can\'t find a project named Banana', output[0])

    prompt.do_project('Banana 2')
    with Capturing() as output:
        prompt.do_list('Banana')
    assert_in(u'Banana has a target goal of $2', output[0])


def test_projects():
    prompt = MiniKickstarterPrompt()
    prompt.do_projects(prompt)

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"