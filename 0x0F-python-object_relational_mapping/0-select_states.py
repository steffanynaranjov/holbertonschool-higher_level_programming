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

    cur.execute('SELECT * FROM states ORDER BY id;')
    row = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()
