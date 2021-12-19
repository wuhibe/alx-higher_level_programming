#!/usr/bin/python3
''' script for task 5 '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT name FROM cities WHERE (SELECT id FROM states WHERE
                BINARY name = %s) = state_id""", (sys.argv[4],))
    states = cur.fetchall()
    print(", ".join([state[0] for state in states]))
    cur.close()
    db.close()
