from cmd import Cmd
from painter import paint

def show_logo():
    file = open('logo.txt', 'r')
    logo = file.read()
    print (paint.green(logo))

class MiniKickstarterPrompt(Cmd):


    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print "Hello, %s" % name

    def do_quit(self, args):
        """Quits Mini Kickstarter."""
        print "Quitting."
        raise SystemExit


if __name__ == '__main__':
    prompt = MiniKickstarterPrompt()
    prompt.prompt = '> '
    show_logo()
    prompt.cmdloop('Starting Mini Kickstarter...')
