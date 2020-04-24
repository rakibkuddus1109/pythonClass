# For mySql : pymysql/mysqlclient/mySqlDb etc. (connectors)
# mongo db : pymongo

import pymysql

conn = pymysql.connect(user='root',password='',host='localhost',database='Python_class')  # to establish DB connection

cur = conn.cursor()  # setup a curosr object

# cur.execute("create database Python_Class")  # DB would not be setup runtime by code in real scenario, it should already be there
# cur.execute ("create table emp_personal(emp_name varchar(20),emp_email varchar(20),emp_city varchar(20))")

# cur.execute("insert into emp_personal values ('Rakib','rk@gmail.com','Hyderabad'),('Kaniz','kt@gmail.com','Bengaluru'),('Rafaat','rt@gmail.com','Kolkata')")

# conn.commit()

cur.execute("select * from emp_personal")
# row = cur.fetchone()
row = cur.fetchall()
print(row)
conn.close()  # to close the opened DB connection