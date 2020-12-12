#!/usr/bin/python3
"""
connect the mysql
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    q = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id ORDER BY cities.id;
    """

    cur.execute(q)
    [print(state) for state in cur.fetchall()]

    cur.close()
    conn.close()
