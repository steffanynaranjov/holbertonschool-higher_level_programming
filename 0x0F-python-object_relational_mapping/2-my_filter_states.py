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

    cur.execute("SELECT states.id, name FROM states WHERE BINARY name = '{}';"
                .format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()
