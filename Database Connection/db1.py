# Python Database Connectivity.

import mysql.connector

# to use a perticular database use database = "dbname"
mydb = mysql.connector.connect(host = "localhost", user  = "", passwd = "", database = "")
mycursor = mydb.cursor()
mycursor.execute("select * from <tablename>")   # table name(salesman)

res = mycursor.fetchall()   # fetches all the data from mycursor.
for i in res:
    print(i)

