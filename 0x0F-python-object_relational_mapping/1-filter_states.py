#!/usr/bin/python3
''' this is a script for task 1 '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
