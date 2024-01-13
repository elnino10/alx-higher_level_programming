#!/usr/bin/python3
"""
module for a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys

import MySQLdb


def filter_cities(usr, passwd, db_name, state_name):
    """lists all the cities in a state

    Args:
        usr (string): mysql username
        passwd (string): mysql password
        db_name (string): database name
        state_name (string): state name
    """
    db_conn = MySQLdb.connect(
        host="localhost", port=3306, user=usr, passwd=passwd, db=db_name
    )
    cursor = db_conn.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states "
    query += "ON cities.state_id = states.id "
    query += "AND states.name = %s ORDER BY cities.id"
    cursor.execute(query, (state_name,))
    data = cursor.fetchall()

    query_list = []
    for val in data:
        query_list += val

    i = 0
    while i < len(query_list):
        if i == len(query_list) - 1:
            print(query_list[i])
        else:
            print(f"{query_list[i]}, ", end="")
        i += 1

    cursor.close()
    db_conn.close()


if __name__ == "__main__":
    username, password, database, state = sys.argv[1:5]
    filter_cities(username, password, database, state)
