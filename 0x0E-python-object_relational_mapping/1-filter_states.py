#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(user=sys.argv[1],
                         host="localhost",
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    myCursor = db.cursor()
    myCursor.execute("SELECT * FROM states ORDER BY id  ASC")
    for i in myCursor.fetchall():
        if i[1][0] == 'N':
            print(i)
    db.close()
