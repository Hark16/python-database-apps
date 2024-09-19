import sqlite3
    
conn = sqlite3.connect('employee.db'); 
print ("Opened database successfully");
cur = conn.cursor()



d=int(input("how many member you wanna add: "))


for a in range(d):
    
    name=input ("enter your name: ");
    salary= str(input("enter your salary: "));
    a=conn.execute("INSERT INTO emplo(NAME,SALARY) \
    VALUES( \"" + name + "\", " +salary +")");


conn.commit()
print("name\t, salary")
c=cur.execute("SELECT* FROM emplo")
for q in c:
    print(q[0],"\t",q[1],"")
    

print ("Records created successfully");
conn.close()