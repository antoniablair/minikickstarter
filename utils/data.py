import sqlite3 as sqlite


def query_db(query_string, args=None, silent=False, fetch_one=False, commit=False):
    """Helper function to query the database."""
    result = None
    con = None

    try:
        con = sqlite.connect('test.db')
        # if as_dict:
        con.row_factory = sqlite.Row

        cur = con.cursor()

        if args:
            cur.execute(query_string, args)
        else:
            cur.execute(query_string)

        if commit == True:
            con.commit()

        else:
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

