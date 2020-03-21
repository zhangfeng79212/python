import csv
import os
import codecs
import fabric

date=20200308
ip='47.93.23.227'
password='ZQ7h5@Bt#Ct8'
f=codecs.open("test.csv", "w",'utf-8')
writer=csv.writer(f)
writer.writerow([u'机器名字',date])
def getnumber(ip):
    try:
        conn = fabric.Connection(ip , user = 'root',port = 22, config = None, connect_kwargs={"password": password})
        result=conn.run('ls '+str(date)+'|wc -l')
        number=result.stdout.strip()
        if not number.isdigit():
            number=0
        return number
    except Exception as ex:
        print("execute fail!!")
        print(ex)
        number=0
    finally:
        conn.close()
        return 0
writer.writerow(['ms1xxxx',getnumber(ip)])
writer.writerow(['ms2xxxx','456'])
writer.writerow(['ms3xxxx','456'])
writer.writerow(['ms4xxxx','456'])
writer.writerow(['ms5xxxx','456'])
writer.writerow(['ms6xxxx','456'])
writer.writerow(['ms7xxxx','456'])
writer.writerow(['ms8xxxx','456'])
writer.writerow(['mstotal','456'])
writer.writerow(['media91','456'])
writer.writerow(['media92','456'])
f.close()
