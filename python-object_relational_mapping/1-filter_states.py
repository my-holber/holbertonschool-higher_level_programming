#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    cursor = conn.cursor()
    cursor.execute('''
                   SELECT states.id, states.name
                   FROM states
                   WHERE states.name LIKE 'N%'
                   ORDER BY states.id ASC
                   ''')
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    conn.close()
