import sqlite3
conn = sqlite3.connect('school.db'); 
print ("Opened database successfully");
cur = conn.cursor()

'''cur.execute("DROP TABLE IF EXISTS school")


table= "CREATE TABLE school(rollno int, name str, sex str, class int, section str)"
conn.execute(table);
'''
#print ("table created")

d=int(input("how many data wanna enter: "))

for b in range(d):
    roll=str(input("enter roll number : "))
    name=str(input("name of student: "))
    sex=str(input("what is gender: "))
    clas=str(input("enter class: "))
    section=str(input("what is Section of Class: "))
    b = "INSERT INTO school (rollno, name, sex, class, section) VALUES (?, ?, ?, ?, ?)"
    val=(roll, name, sex, clas, section)
    cur.execute(b, val)
    
conn.commit()

#print(cur.rowcount(),  "data inserted ")

print("roll no\t, name\t, gender\t, class\t, section\t")

c=cur.execute("SELECT*FROM school")

for q in c:
    print(q[0],"\t",q[1],"\t",q[2],"\t",q[3],"\t",q[4],)

print("successful")

conn.close()