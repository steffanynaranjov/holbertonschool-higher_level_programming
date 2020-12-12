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

    cu.execute('SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id;')
    row = cu.fetchall()

    for r in rows:
        print(r)

    cu.close()
    conn.close()
