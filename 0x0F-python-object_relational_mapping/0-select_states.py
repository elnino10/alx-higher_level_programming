#!/usr/bin/python3
"""script lists all states from the database hbtn_0e_0_usa"""

import sys

import MySQLdb


def list_states(username, password, database_name):
    """creates a connection to database and executes query"""
    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=database_name
    )

    # create cursor object to interact with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")


if __name__ == "__main__":
    # get information from the CLI arguments
    usr_name, psswd, db_name = sys.argv[1:4]
    list_states(usr_name, psswd, db_name)
