import sqlite3

#connect to sqllite
connection=sqlite3.connect("student.db")

#create a cursor to insert,create,retreive etc
cursor=connection.cursor()

#create table
table_info="""
create table student(name varchar(25),class varchar(25),section varchar(25),marks int);
"""
cursor.execute(table_info)

#insert records
cursor.execute("insert into student values('arpith','data science','A',90)")
cursor.execute("insert into student values('nischi','c++','B',100)")
cursor.execute("insert into student values('maaki','entreprenur','F',38)")
cursor.execute("insert into student values('ranger','MBA','A',99)")
cursor.execute("insert into student values('ajju','construction','B',85)")

#display records
print("the inserted records are:")

data=cursor.execute("select * from student;")

for row in data:
    print(row)

#close connection
connection.commit()
connection.close()
