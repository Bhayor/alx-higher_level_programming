#!/usr/bin/python3
""" list all states with a name starting with N """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    stmt = db.cursor()
    stmt.execute("""select * from states where name like 'N%' order by id asc""")
    rows = stmt.fetchall()
    for row in rows:
        print(row)
    stmt.close()
    db.close()
