# add the mysql library in python
#pip install pymysql
import pymysql 
#establish the database connection
myconnection = pymysql.connect(
host="localhost",
user="root",
password="srmcem@123",
database="blog"

)

print("database is connected..")

# create my blog table in database
createTable="""
create table if not exists blogtable
(id int auto_increment primary key,
title text, description text, name varchar(255))
"""
cursor = myconnection.cursor()
cursor.execute(createTable)
print("Table is created successfully")
# insert blog in database...
# insertBlog="""
# insert into blogtable(title,description,name ) values
# (%s,%s,%s)
# """
# data=(input("Enter name"),
#       input("enter description"),
#       input("enter author name"))
# cursor.execute(insertBlog,data)
# myconnection.commit()
# print("blog inserted....")

# to get the data from the tabble........
getblogs='SELECT * from blogtable'
cursor.execute(getblogs)
data =cursor.fetchall()
for row in data:
    print(row)