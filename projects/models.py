from painter import paint
import sqlite3 as sqlite
import sys

class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.currently_raised = 0


    def save_or_update(self, new_currently_raised, query_set):
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            qs = query_set

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


    def update(self, new_currently_raised):
        qs = u'UPDATE Projects SET currently_raised={} ' \
             u'WHERE name=\'{}\''.format(new_currently_raised, self.name)

        self.save_or_update(new_currently_raised, qs)


    def save(self):
        qs = u"INSERT INTO {tn} ({cn1}, {cn2}, {cn3}) " \
             u"VALUES (\'{name}\',{target},{cr});".format(tn='Projects', cn1 = 'name', cn2 = 'target',
                                                          cn3 = 'currently_raised', name = self.name,
                                                          target = self.target, cr = self.currently_raised)

        self.save_or_update(self.currently_raised, qs)

    def __str__(self):
        return self.name
