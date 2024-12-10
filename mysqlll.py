import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="myfile"


)

mycursor = mydb.cursor()






sql = "INSERT INTO myfamily (name,age,place)VALUES (%s,%s,%s) "
val = [
    ("kunjumon",60,"kayamkulam"),
    ("girija",54,"TVM"),
    ("akhila",32,"bnglr"),
    ("anila",28,"ekm")
]

mycursor.executemany(sql,val)
mydb.commit()


