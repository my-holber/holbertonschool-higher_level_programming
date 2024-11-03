#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    name = sys.argv[4]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id".format(name))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    conn.close()
