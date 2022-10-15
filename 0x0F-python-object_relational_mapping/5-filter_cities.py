#!/usr/bin/python3
""" list all cities by state from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    stmt = db.cursor()
    arg = sys.argv[4]
    stmt.execute("""select cities.name from cities left join states 
            on cities.state_id=states.id where states.name = %s order by cities.id asc """, (arg, ))
    rows = stmt.fetchall()
    cityList = list(row[0] for row in rows)
    print(*cityList, sep=", ")
    stmt.close()
    db.close()
