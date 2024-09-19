import sqlite3
conn = sqlite3.connect('family.db'); 

print ("Ragister Opened successfully");

cur = conn.cursor()



d=int(input("how many member you wanna add: "))

for a in range(d):
    name=str(input ("enter name of member: "));
    father=str(input("father's name: "));
    mother=str(input("mother's name: "));
    birth=str(input("Date of Birth: "));
    age=str(input("Age is: "));
    relationship=input("what is relationship with you: ");
    home=input("HomeTown is: ");
    mobile=str(input("Mobile Number: "));
    mail=str(input("E-Mail Id; "));
    job=input("Ocupation: ");
    a= "INSERT INTO family(name ,father ,mother ,birth ,age ,relationship ,hometown ,mobile ,mailId ,ocupation) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    val=(name, father, mother, birth, age, relationship, home, mobile, mail, job)
    
    cur.execute(a, val)
conn.commit()

print("Name\t,F.name\t,M.name\t,D of B\t,Age\t,Relationship\t,HomeTown\t,Mob.number\t,Mail\t,Ocupation")

c=cur.execute("SELECT* FROM family")

for q in c:
    print(q[0],"\t",q[1],"\t",q[2],"\t",q[3],"\t",q[4],"\t",q[5],"\t",q[6],"\t",q[7],"\t",q[8],"\t",q[9],)
    

'''print("name\t, salary")
    
c=cur.execute("SELECT* FROM emplo")
    
for q in c:
    print(q[0],"\t",q[1],"")
    

'''
print ("Records created successfully");

conn.close()