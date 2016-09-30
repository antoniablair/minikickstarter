import sqlite3 as sqlite


def query_db(table, lookup_col, query_word, query_all=False):
    """
    Find row(s) by a query word and return everything inside it.
    Set query_all to true to return all rows in the table.
    """
    rows = None
    con = None

    try:
        # todo: Fix all the test.dbs everywhere
        con = sqlite.connect('test.db')
        cur = con.cursor()

        if query_all == False:
            query_string = u'SELECT * FROM {tn} WHERE {col}=\'{qw}\';'.format(tn=table, col=lookup_col, qw=query_word)
            print query_string
            cur.execute(query_string)
            rows = cur.fetchone()
        else:
            query_string = u'SELECT * FROM {tn};'.format(tn=table)
            cur.execute(query_string)
            rows = cur.fetchall()
    except sqlite.Error, e:
        # if con:
        #     con.rollback()
        print u'This is being called'
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()
            return rows


def alt_query(query_string, silent=False, as_dict=False, fetch_one=False):
    """Helper function to query the database."""
    result = None
    con = None

    try:
        # todo: Fix all the test.dbs everywhere
        con = sqlite.connect('test.db')
        if as_dict:
            con.row_factory = sqlite.Row

        cur = con.cursor()

        query_string = query_string
        cur.execute(query_string)

        if fetch_one == True:
            print 'only fetches one'
            result = cur.fetchone()
        else:
            result = cur.fetchall()

    except sqlite.Error, e:
        # if con:
        #     con.rollback()
        if not silent:
            print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()
            return result



# def fetch_project_dict(name):
#     row = None
#
#     try:
#         table = 'Projects'
#         lookup_col = 'name'
#         query_word = name
#
#         con = sqlite.connect('test.db')
#         con.row_factory = sqlite.Row
#         cur = con.cursor()
#         cur.execute("SELECT * FROM Projects")
#
#         rows = cur.fetchall()
#
#         # row = query_db(table, lookup_col, query_word)
#         for row in rows:
#             print row["name"]
#
#     except sqlite.Error, e:
#         if con:
#             con.rollback()
#         row = False
#         print "Error %s:" % e.args[0]
#         sys.exit(1)
#
#     finally:
#         if con:
#             con.close()
#         return row