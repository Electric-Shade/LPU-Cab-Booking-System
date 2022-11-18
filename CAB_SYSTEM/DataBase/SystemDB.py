import mysql.connector
objectDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Veracita@19!",
    database="CBS"
)

instance = objectDB.cursor()
# instance.execute("CREATE TABLE LogDetails (name varchar(255), username varchar(255),gender varchar(6), mobile varchar(12), Uid int(12), email varchar(255), password varchar(10))")
# instance.execute("show tables")
instance.execute("CREATE TABLE BookDetails(bmobile varchar(10), buid int(10), bfrom varchar(255), bto varchar(255), bday varchar(15), btime int(10), otp int(4))")
# instance.execute("drop table BookDetails")

