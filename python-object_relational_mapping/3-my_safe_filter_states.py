#!/usr/bin/python3
"""
    Script that lists all states from the database where the name matches the given argument.
    The script is safe from SQL injections.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Подключение к базе данных
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name = sys.argv[4]
    cursor = conn.cursor()
    
    # Подготовка запроса с защитой от SQL-инъекций
    query = (
        "SELECT states.id, states.name "
        "FROM states "
        "WHERE states.name LIKE BINARY %s "
        "ORDER BY states.id ASC"
    )
    
    # Передача параметра как кортежа из одного элемента
    cursor.execute(query, (name,))

    # Вывод результата
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Закрытие курсора и подключения
    cursor.close()
    conn.close()

