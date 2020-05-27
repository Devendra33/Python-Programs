# Python Database Connectivity.

import mysql.connector

# to use a perticular database use database = "dbname"
mydb = mysql.connector.connect(host = "localhost", user  = "root", passwd = "Hondadio@1", database = "tsp")
mycursor = mydb.cursor()
mycursor.execute("select * from salesman")   # table name(salesman)

res = mycursor.fetchall()
for i in res:
    print(i)

