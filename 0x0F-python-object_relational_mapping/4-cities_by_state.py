#!/usr/bin/python3
''' script for task 4 '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities,
                states WHERE cities.state_id = states.id;""")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
