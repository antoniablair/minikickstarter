import sqlite3 as sqlite

def query_db(query_string, silent=False, as_dict=False, fetch_one=False):
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
            result = cur.fetchone()
        else:
            result = cur.fetchall()

    except sqlite.Error, e:
        if not silent:
            print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()
            return result

