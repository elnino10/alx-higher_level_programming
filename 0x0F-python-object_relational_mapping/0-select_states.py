#!/usr/bin/python3
"""script lists all states from the database hbtn_0e_0_usa"""

import sys

import MySQLdb


def list_states(u_name, password, db_name):
    """creates a connection to database and executes query"""
    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=u_name, passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    all_states = cur.fetchall()

    for state in all_states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    # get information from the CLI arguments
    usr_name, psswd, database_name = sys.argv[1:4]
    list_states(usr_name, psswd, database_name)
