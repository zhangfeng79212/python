import csv
import os
import codecs
import fabric
import datetime
import schedule
import time
import yagmail
import json

def job():
    print("I'm working...")
    now = datetime.datetime.now()

    oneday = datetime.timedelta(days=1)
    today = datetime.date.today()
    yestoday = today - oneday

    ts = yestoday.strftime('%Y%m%d')
    date=ts
    filename1="test"+str(date)+".csv"
    f=codecs.open("test"+str(date)+".csv", "w",'utf-8')
    writer=csv.writer(f)
    writer.writerow([u'机器名字',date])
    def getnumber(ip,hosttype):
        try:
            if hosttype=='ms':
                conn = fabric.Connection(ip, user='ms', port=22, config=None, connect_kwargs={"password": 'cintel1234!@#$'})
                result=conn.run('ls /home/ms/cin/voxdst/media/800002/ccrecord/'+str(date)+'|wc -l')
            if hosttype=='media':
                conn = fabric.Connection(ip, user='media', port=22, config=None, connect_kwargs={"password": 'cintel123'})
                result = conn.run('ls /home/media/media/800002/ccrecord/' + str(date) + '|wc -l')
            if hosttype== 'media1':
                conn = fabric.Connection(ip, user='media', port=22, config=None, connect_kwargs={"password": '123456'})
                result = conn.run('ls /home/media/media/666666/ccrecord/' + str(date) + '|wc -l')
            if hosttype=='ms1':
                conn = fabric.Connection(ip, user='ms', port=22, config=None, connect_kwargs={"password": 'cintel1234!@#$'})
                result=conn.run('ls /home/ms/cin/voxdst/media/666666/ccrecord/'+str(date)+'|wc -l')
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
            return number
    ms1n=getnumber('10.30.2.101','ms')
    writer.writerow(['ms1node2',ms1n])
    ms2n=getnumber('10.30.2.102','ms')
    writer.writerow(['ms2node2',ms2n])
    ms3n=getnumber('10.30.2.103','ms')
    writer.writerow(['ms3node2',ms3n])
    ms4n=getnumber('10.30.2.104','ms')
    writer.writerow(['ms4node2',ms4n])
    ms5n=getnumber('10.30.2.105','ms')
    writer.writerow(['ms5node2',ms5n])
    ms6n=getnumber('10.30.2.106','ms')
    writer.writerow(['ms6node2',ms6n])
    ms7n=getnumber('10.30.2.107','ms')
    writer.writerow(['ms7node2',ms7n])
    ms8n=getnumber('10.30.2.108','ms')
    writer.writerow(['ms8node2',ms8n])
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)
    writer.writerow(['mstotal',msxn])
    media91n=getnumber('10.30.2.91','media')
    writer.writerow(['media91',media91n])
    media92n=getnumber('10.30.2.92','media')
    writer.writerow(['media92',media92n])
    contents1={ "ms1":ms1n,
                "ms2":ms2n ,
                "ms3":ms3n,
                "ms4":ms4n,
                "ms5":ms5n,
                "ms6":ms6n,
                "ms7":ms7n,
                "ms8":ms8n,
                "mstotal":msxn,
                "media1":media91n,
                "media2":media92n}
    ##node3
    ms1n=getnumber('10.30.3.101','ms')
    writer.writerow(['ms1node3',ms1n])
    ms2n=getnumber('10.30.3.102','ms')
    writer.writerow(['ms2node3',ms2n])
    ms3n=getnumber('10.30.3.103','ms')
    writer.writerow(['ms3node3',ms3n])
    ms4n=getnumber('10.30.3.104','ms')
    writer.writerow(['ms4node3',ms4n])
    ms5n=getnumber('10.30.3.105','ms')
    writer.writerow(['ms5node3',ms5n])
    ms6n=getnumber('10.30.3.106','ms')
    writer.writerow(['ms6node3',ms6n])
    ms7n=getnumber('10.30.3.107','ms')
    writer.writerow(['ms7node3',ms7n])
    ms8n=getnumber('10.30.3.108','ms')
    writer.writerow(['ms8node3',ms8n])
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)
    writer.writerow(['mstotal',msxn])
    media91n=getnumber('10.30.3.91','media')
    writer.writerow(['media91',media91n])
    media92n=getnumber('10.30.3.92','media')
    writer.writerow(['media92',media92n])
    contents2= {"ms1": ms1n,
                 "ms2": ms2n,
                 "ms3": ms3n,
                 "ms4": ms4n,
                 "ms5": ms5n,
                 "ms6": ms6n,
                 "ms7": ms7n,
                 "ms8": ms8n,
                 "mstotal": msxn,
                 "media1": media91n,
                 "media2": media92n}
    #node1

    f.close()
    #发邮件出去
    print(contents1)
    print(contents2)
    yag = yagmail.SMTP(user='48965793@qq.com', password='qowsjbxjkjeybgfc', host='smtp.qq.com')
    yag.send('zhangfeng79212@163.com', subject="广东德律", contents=[ts,json.dumps(contents1),json.dumps(contents2)])

schedule.every().day.at("04:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
