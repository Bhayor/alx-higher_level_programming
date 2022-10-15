#!/usr/bin/python3
""" list all cities by state from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    stmt = db.cursor()
    stmt.execute("select cities.id, cities.name, states.name from cities left join states on cities.state_id=state_id order by cities.id asc ")
    rows = stmt.fetchall()
    for row in rows:
        print(row)
    stmt.close()
    db.close()
