#!/usr/bin/python3
"""
module with a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
import sys

import MySQLdb


def filter_states(usr, passwd, db_name, state_name):
    """displays values where state name matches state_name

    Args:
        usr (string): mysql username
        passwd (string): mysql password
        db_name (string): database name
        state_name (string): state to search for
    """

    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=usr, passwd=passwd, db=db_name
    )
    cursor = db_conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC"
    cursor.execute(query.format(state_name))
    data = cursor.fetchall()

    for val in data:
        print(val)

    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    u_name, password, database, state = sys.argv[1:5]
    filter_states(u_name, password, database, state)
