#!/usr/bin/python3
"""
module for a script that lists all cities from the database hbtn_0e_4_usa
"""
import sys

import MySQLdb


def cities_by_states(usr, passwd, db_name):
    """lists all cities from database

    Args:
        usr (string): mysql username
        passwd (string): mysql password
        db_name (string): database name
    """

    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=usr, passwd=passwd, db=db_name
    )
    cursor = db_conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities, states "
    query += "WHERE cities.state_id = states.id ORDER BY id"
    cursor.execute(query)
    data = cursor.fetchall()

    for val in data:
        print(val)

    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    cities_by_states(username, password, database)
