#!/usr/bin/python3
'''Write a script that takes in the name of a state as an
argument and lists all cities of that state'''

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states \
            ON states.id = cities.state_id \
            WHERE states.name = %s", (sys.argv[4],))

    rows = cur.fetchall()

    total = ', '.join(row[0] for row in rows)

    print(total)

    cur.close()
    db.close()
