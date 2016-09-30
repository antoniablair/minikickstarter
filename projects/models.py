import sqlite3 as sqlite
import sys

class Project():
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.currently_raised = 0.0

    def funds_needed(self):
        print 'inside funds_needed'
        sum = target - float
        print sum
        return sum

    # def save(self):
    #     print u'Saving'
    #     try:
    #         with open(LOCAL_DATA, 'w') as db:
    #             db.write(string_from_data(self.name))
    #     except:
    #         print u'that did not work'

    def update(self, new_currently_raised):
        print ('inside update')
        try:
            print 'in try loop'
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
            cur.execute("INSERT INTO Projects (name, target, currently_raised)values(?,?,?,);",
                        (name, target, currently_raised))

            con.commit()
            return True
        except sqlite.Error, e:
            if con:
                con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
            return False

    def __str__(self):
        return self.name
