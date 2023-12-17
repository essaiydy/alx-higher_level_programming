#!/usr/bin/python3
"""script that takes in an argument and
displays all values in the states table"""


if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("select * from states where name = '{}'".format(sys.argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
