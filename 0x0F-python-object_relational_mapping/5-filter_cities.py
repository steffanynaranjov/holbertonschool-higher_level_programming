#!/usr/bin/python3
"""
connect the mysql
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cu = conn.cursor()

    cu.execute('SELECT cities.name FROM cities'
               ' INNER JOIN states ON cities.state_id = states.id'
               ' WHERE states.name LIKE BINARY %s'
               ' ORDER BY cities.id ASC;', (argv[4],))
    row = cu.fetchall()

    print(", ".join([row[0] for row in rows]))

    cu.close()
    conn.close()
