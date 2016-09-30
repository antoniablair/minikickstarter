import sqlite3 as sqlite

from backings.actions import *

# def create_backing(backer, project_name, card, amount):
#     print u'INside create backing'
#     try:
#         con = sqlite.connect('test.db')
#         cur = con.cursor()
#         cur.execute("INSERT INTO Backings (name, project, card, amount)values(?,?,?,?);", (backer, project_name, card, amount))
#
#         con.commit()
#         return True
#     except sqlite.Error, e:
#         if con:
#             con.rollback()
#         print "Error %s:" % e.args[0]
#         sys.exit(1)
#     finally:
#         if con:
#             con.close()
#         return False

class Backing():
    def __init__(self, name, project, card, amount):
        self.name = name
        self.project = project
        self.card = card
        self.amount = amount

    def save(self):
        try:
            con = sqlite.connect('test.db')
            cur = con.cursor()
            cur.execute("INSERT INTO Backings (name, project, card, amount)values(?,?,?,?);",
                        (self.name, self.project, self.card, self.amount))

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
        return u'{} - {}'.format(self.name, self.project)