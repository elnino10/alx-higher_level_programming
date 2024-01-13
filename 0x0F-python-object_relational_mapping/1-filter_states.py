#!/usr/bin/python3
"""
module is for a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import sys

import MySQLdb


def states_startswith_n(usrname, psswd, db_name):
    """list all states with name starting with N

    Args:
        usrname (string): mysql username
        psswd (string): mysql password
        db_name (string): database name
    """
    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=usrname, passwd=psswd, db=db_name
    )

    cursor = db_conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, ("N" + "%",))
    list_states = cursor.fetchall()

    for state in list_states:
        print(state)

    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    states_startswith_n(username, password, database)
