#!/usr/bin/python3
''' script for task 2 '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{:s}'"
                .format(sys.argv[4])+"ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
