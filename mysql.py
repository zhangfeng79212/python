import pymysql
conn=pymysql.connect(host="60.205.178.238",port=3300,user="cincc",password="cinCC1234",database="day17",charset="utf8")
cursor=conn.cursor()
ret=cursor.execute("select * from user")
results=cursor.fetchall()
for row in results:
    id=row[0]
    name=row[1]
    addr=row[5]
    print(id,name,addr)
print("{} rows in set.".format(ret))
cursor.close()
conn.close()
