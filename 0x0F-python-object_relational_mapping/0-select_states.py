#!/usr/bin/python3
''' this is script to task 0 '''


import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=uname,
                         passwd=pwd, db=database, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
