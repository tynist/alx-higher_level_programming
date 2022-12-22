#!/usr/bin/python3
"""SelectStates module"""
import MySQLdb
import sys


def select_states():
    """Grabs states from database"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         pwrd=password,
                         datab=database
                         )
    cur = datab.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = curr.fetchall()
    for row in rows:
        print(row)
    cur.close()
    datab.close()


if __name__ == "__main__":
    select_states()
