import sqlite3

db=sqlite3.connect("mydata.db")

print("database created")

cursor= db.cursor()
cursor.execute("DROP TABLE IF EXISTS LIST")

createTable = "CREATE TABLE LIST(id int, FirstName varchar(32), LastName varchar(32), dept int)"
cursor.execute(createTable)


print("table created")

db.close()