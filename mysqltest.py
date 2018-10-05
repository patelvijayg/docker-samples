#python -m pip install mysql-connector
#CREATE TABLE testing (id INT(6) PRIMARY KEY,name VARCHAR(100) NOT NULL,salary DECIMAL(10,2),birthdate DATE)
#insert into testing (id,name,salary,birthdate) values(1,'vijay',100.01,'1981-03-27')
import mysql.connector
mydb = mysql.connector.connect(
  host="db4free.net",
  user="mysqluser_vijay",
  passwd="aabb1122ccdd",
  database="mysqldb_vijay"
)

def deleteone(id):
	mycursor = mydb.cursor()
	sql = "DELETE FROM testing WHERE id = %s"
	adr = (id, )
	mycursor.execute(sql, adr)
	print(mycursor.rowcount, "record(s) deleted")
	
def insertone():
	mycursor = mydb.cursor()
	sql = "insert into testing (id,name,salary,birthdate) VALUES (%s, %s, %s, %s)"
	val = [(2,'vijay2',100.01,'1981-03-27'),(3,'vijay3',100.01,'1981-03-27')]
	mycursor.executemany(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "was inserted.")

def selectdata():
	mycursor = mydb.cursor()
	sql = "SELECT * FROM testing"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

insertone()
selectdata()
deleteone(2)
selectdata()

#print(json.dumps(x, indent=4, sort_keys=True,separators=(",", ":")))
