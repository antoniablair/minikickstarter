from painter import paint
import sqlite3 as sqlite
import sys

class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.currently_raised = 0


    def update(self, new_currently_raised):
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()

            print new_currently_raised
            print self.name
            qs = u'UPDATE Projects SET currently_raised={} WHERE name=\'{}\''.format(new_currently_raised, self.name)

            cur.execute(qs)

            con.commit()
            row = cur.fetchone()
        except sqlite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()


    def save(self):
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            qs = u"INSERT INTO {tn} ({cn1}, {cn2}, {cn3}) " \
                 u"VALUES (\'{name}\',{target},{cr});".format(tn='Projects', cn1 = 'name', cn2 = 'target',
                                                              cn3 = 'currently_raised', name = self.name,
                                                              target = self.target, cr = self.currently_raised)

            cur.execute(qs)
            con.commit()
        except sqlite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()

    def __str__(self):
        return self.name
