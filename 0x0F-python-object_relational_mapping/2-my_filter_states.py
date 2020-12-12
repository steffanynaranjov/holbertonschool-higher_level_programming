#!/usr/bin/python3
"""
name that match with arg
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cu = conn.cursor()

    c = 'SELECT * FROM states WHERE name LIKE BINARY "{}"' \
        ' ORDER BY states.id ASC;'
    c = c.format(argv[4])
    cu.execute(c)

    row = cu.fetchall()

    for r in rows:
        print(r)

    cu.close()
    conn.close()
