#!/usr/bin/python3
"""
script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, script should be safe from MySQL injections!
"""
import sys

import MySQLdb


def safe_filter_states(usr, passwd, db_name, state_name):
    """filters values in a table safe from MySQL injection

    Args:
        usr (string): mysql username
        passwd (string): mysql password
        db_name (string): database name
        state_name (string): state name searched
    """
    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=usr, passwd=passwd, db=db_name
    )
    cursor = db_conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name=%s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    for val in data:
        print(val)

    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    username, password, database, state = sys.argv[1:5]
    safe_filter_states(username, password, database, state)
