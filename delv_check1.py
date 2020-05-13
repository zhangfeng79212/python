import csv
import os
import codecs
import fabric
import datetime
import schedule
import time
import yagmail
import json

dict1List=[{"ip": "192.168.14.141", "username": "acd", "password": "cintel1234!@#$"},
            {"ip": "192.168.14.141", "username": "acd", "password": "cintel1234!@#$"}
           ]
#dict1={"ip":"60.205.178.238","username":"root","password":"abc123.com"}
dict2List=[
            {"ip": "10.30.1.21", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.22", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.21", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.22", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.21", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.22", "username": "acd", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.23", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.24", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.23", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.24", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.23", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.24", "username": "cti", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.31", "username": "smp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.32", "username": "smp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.31", "username": "smp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.32", "username": "smp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.31", "username": "smp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.32", "username": "smp", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.51", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.52", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.51", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.52", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.51", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.52", "username": "sbc", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.1.71", "username": "media", "password": "123456","port":"22"},
            {"ip": "10.30.1.72", "username": "media", "password": "123456","port":"50022"},
            {"ip": "10.30.2.91", "username": "media", "password": "cintel123","port":"22"},
            {"ip": "10.30.2.92", "username": "media", "password": "cintel123","port":"22"},
            {"ip": "10.30.3.91", "username": "media", "password": "cintel123","port":"22"},
            {"ip": "10.30.3.92", "username": "media", "password": "cintel123","port":"22"},
            {"ip": "10.30.1.81", "username": "lamp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.2.81", "username": "lamp", "password": "cintel1234!@#$","port":"22"},
            {"ip": "10.30.3.81", "username": "lamp", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.101", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.102", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.103", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.104", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.105", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.106", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.107", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.1.108", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.101", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.102", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.103", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.104", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.105", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.106", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.107", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.2.108", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.101", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.102", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.103", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.104", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.105", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.106", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.107", "username": "ms", "password": "cintel1234!@#$","port":"22"},
    {"ip": "10.30.3.108", "username": "ms", "password": "cintel1234!@#$","port":"22"}

            ]
def job1(ts1):
    print("I'm working...")


    date=ts1

    def getnumber(ip,hosttype,port=22):
        try:
            if hosttype=='ms':
                conn = fabric.Connection(ip, user='ms', port=port, config=None, connect_kwargs={"password": 'cintel1234!@#$'})
                result=conn.run('ls /home/ms/cin/voxdst/media/800002/ccrecord/'+str(date)+'|wc -l')
            if hosttype=='media':
                conn = fabric.Connection(ip, user='media', port=port, config=None, connect_kwargs={"password": 'cintel123'})
                result = conn.run('ls /home/media/media/800002/ccrecord/' + str(date) + '|wc -l')
            if hosttype== 'media5002':
                conn = fabric.Connection(ip, user='media', port=port, config=None, connect_kwargs={"password": '123456'})
                result = conn.run('ls /home/media/media/666666/servicerecord/000001666666005002/' + str(date) + '|wc -l')
            if hosttype=='ms5002':
                conn = fabric.Connection(ip, user='ms', port=port, config=None, connect_kwargs={"password": 'cintel1234!@#$'})
                result=conn.run('ls /home/ms/cin/voxdst/media/666666/servicerecord/000001666666005002/'+str(date)+'|wc -l')
            if hosttype == 'media6004':
                conn = fabric.Connection(ip, user='media', port=port, config=None, connect_kwargs={"password": '123456'})
                result = conn.run('ls /home/media/media/666666/servicerecord/000001666666006004/' + str(date) + '|wc -l')
            if hosttype == 'ms6004':
                conn = fabric.Connection(ip, user='ms', port=port, config=None,connect_kwargs={"password": 'cintel1234!@#$'})
                result = conn.run('ls /home/ms/cin/voxdst/media/666666/servicerecord/000001666666006004/' + str(date) + '|wc -l')
            if hosttype == 'ms6004n':
                conn = fabric.Connection(ip, user='ms1', port=port, config=None, connect_kwargs={"password": 'cintel1234!@#$'})
                result = conn.run( 'ls /home/ms1/cin/voxdst/media/666666/servicerecord/000001666666006004/' + str(date) + '|wc -l')

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

#node1---5002
    ms1n=getnumber('10.30.1.101','ms5002')
    ms2n=getnumber('10.30.1.102','ms5002')
    ms3n=getnumber('10.30.1.103','ms5002')
    ms4n=getnumber('10.30.1.104','ms5002')
    ms5n=getnumber('10.30.1.105','ms5002')
    ms6n=getnumber('10.30.1.106','ms5002')
    ms7n=getnumber('10.30.1.107','ms5002')
    ms8n=getnumber('10.30.1.108','ms5002')
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)
    media91n=getnumber('10.30.1.71','media5002')
    media92n=getnumber('10.30.1.72','media5002','50022')
    contents5002={ "ms1":ms1n,
                "ms2":ms2n ,
                "ms3":ms3n,
                "ms4":ms4n,
                "ms5":ms5n,
                "ms6":ms6n,
                "ms7":ms7n,
                "ms8":ms8n,
                "mstotal":msxn,
                "media71":media91n,
                "media72":media92n}
#node1---6004
    ms1n=getnumber('10.30.1.101','ms6004')
    ms1nn=getnumber('10.30.1.101','ms6004n')
    ms2n=getnumber('10.30.1.102','ms6004')
    ms2nn=getnumber('10.30.1.102','ms6004n')
    ms3n=getnumber('10.30.1.103','ms6004')
    ms3nn=getnumber('10.30.1.103','ms6004n')
    ms4n=getnumber('10.30.1.104','ms6004')
    ms4nn=getnumber('10.30.1.104','ms6004n')
    ms5n=getnumber('10.30.1.105','ms6004')
    ms5nn=getnumber('10.30.1.105','ms6004n')
    ms6n=getnumber('10.30.1.106','ms6004')
    ms6nn=getnumber('10.30.1.106','ms6004n')
    ms7n=getnumber('10.30.1.107','ms6004')
    ms7nn=getnumber('10.30.1.107','ms6004n')
    ms8n=getnumber('10.30.1.108','ms6004')
    ms8nn=getnumber('10.30.1.108','ms6004n')
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)\
    +int(ms1nn)+int(ms2nn)+int(ms3nn)+int(ms4nn)+int(ms5nn)+int(ms6nn)+int(ms7nn)+int(ms8nn)
    print("maxn"+str(msxn))
    media91n=getnumber('10.30.1.71','media6004')
    media92n=getnumber('10.30.1.72','media6004','50022')
    contents6004={ "ms1":ms1n+"**"+ms1nn,
                "ms2":ms2n+"**"+ms2nn ,
                "ms3":ms3n+"**"+ms3nn,
                "ms4":ms4n+"**"+ms4nn,
                "ms5":ms5n+"**"+ms5nn,
                "ms6":ms6n+"**"+ms6nn,
                "ms7":ms7n+"**"+ms7nn,
                "ms8":ms8n+"**"+ms8nn,
                "mstotal":msxn,
                "media71":media91n,
                "media72":media92n}
#node2
    ms1n=getnumber('10.30.2.101','ms')
    ms2n=getnumber('10.30.2.102','ms')
    ms3n=getnumber('10.30.2.103','ms')
    ms4n=getnumber('10.30.2.104','ms')
    ms5n=getnumber('10.30.2.105','ms')
    ms6n=getnumber('10.30.2.106','ms')
    ms7n=getnumber('10.30.2.107','ms')
    ms8n=getnumber('10.30.2.108','ms')
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)
    media91n=getnumber('10.30.2.91','media')
    media92n=getnumber('10.30.2.92','media')
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
    ms2n=getnumber('10.30.3.102','ms')
    ms3n=getnumber('10.30.3.103','ms')
    ms4n=getnumber('10.30.3.104','ms')
    ms5n=getnumber('10.30.3.105','ms')
    ms6n=getnumber('10.30.3.106','ms')
    ms7n=getnumber('10.30.3.107','ms')
    ms8n=getnumber('10.30.3.108','ms')
    msxn=int(ms1n)+int(ms2n)+int(ms3n)+int(ms4n)+int(ms5n)+int(ms6n)+int(ms7n)+int(ms8n)
    media91n=getnumber('10.30.3.91','media')
    media92n=getnumber('10.30.3.92','media')
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


    #发邮件出去
    print(contents1)
    print(contents2)
    return contents1,contents2,contents5002,contents6004
#    yag = yagmail.SMTP(user='48965793@qq.com', password='qowsjbxjkjeybgfc', host='smtp.qq.com')
#    yag.send('zhangfeng79212@163.com', subject="广东德律", contents=[ts1,json.dumps(contents1),json.dumps(contents2)])
def getSpaceOne(dict):
        try:
            pass
        except Exception as ex:
            pass
        conn = fabric.Connection(dict['ip'], user=dict['username'], port=dict['port'], config=None, connect_kwargs={"password": dict['password']})
        #判断根分区的空间使用情况
        result = conn.run('df -h /|sed -n \'2p\'|awk  \'{print $6  $5}\'',warn=True)
        number = result.stdout.strip()
        dict['rootSpace']=number
        #判断home空间情况
        if(dict['username']=='media'):
            result1 = conn.run('df -h /home/media/media|sed -n \'2p\'|awk  \'{print $6  $5}\'',warn=True)
        else :
            result1 = conn.run('df -h /home|sed -n \'2p\'|awk  \'{print $6  $5}\'',warn=True)
        number1 = result1.stdout.strip()
        dict['homeSpace']=number1
        #判断mysql的同步情况
        if(dict['username'] in ['acd','cti','smp']):
            result2=conn.run('/home/mysql/bin/mysql -ucincc -pcinCC1234 -e "show slave status\G"|grep -A 1 Slave_IO_Running',warn=True)
            number2= result2.stdout.strip()
            dict['mySQL']=number2
        #判断ms同步情况
        if(dict['username'] =='ms'):
            result3=conn.run('ls -t /home/ms/cin/sync/sync*|head -1|cut -d \'/\' -f 6 && cat /home/ms/cin/sync/mergesync.pos',warn=True)
            number3= result3.stdout.strip()
            dict['mergesync-ms']=number3
            if(dict['ip'] in ['10.30.1.101','10.30.1.102','10.30.1.103','10.30.1.104','10.30.1.105','10.30.1.106','10.30.1.107','10.30.1.108']):
                    conn1 = fabric.Connection(dict['ip'], user='ms1', port=dict['port'], config=None,connect_kwargs={"password": dict['password']})
                    result4 = conn1.run('ls -t /home/ms1/cin/sync/sync*|head -1|cut -d \'/\' -f 6 && cat /home/ms1/cin/sync/mergesync.pos',warn=True)
                    number4 = result4.stdout.strip()
                    dict['mergesync-ms1'] = number4
        return dict


def getSpace(dictList):
    for hostDict in dictList:
        try:
            getSpaceOne(hostDict)
            print(json.dumps(hostDict))
        except Exception as ex:
            print('*'*50)
            print(json.dumps(hostDict))
            print(ex)
            print('*'*50)
            continue
    return dictList

def job():
    now = datetime.datetime.now()

    oneday = datetime.timedelta(days=1)
    today = datetime.date.today()
    yestoday = today - oneday
    qiantian=yestoday-oneday

    ts1 = yestoday.strftime('%Y%m%d')
    ts2=qiantian.strftime('%Y%m%d')
    c1,c2,c3,c4=job1(ts1)
    c5,c6,c7,c8=job1(ts2)
    result = getSpace(dict2List)
    str1 = ''
    for dict in dict2List:
        dict.pop('username')
        dict.pop('password')
        str1 += json.dumps(dict) + "\n"
#        print(json.dumps(dict))
    print(str1)
    yag = yagmail.SMTP(user='48965793@qq.com', password='qowsjbxjkjeybgfc', host='smtp.qq.com')
    yag.send('zhangfeng79212@163.com', subject="广东德律",
             contents=[ts1+'node2,node3,node1-5002,node1-6004',json.dumps(c1),json.dumps(c2),json.dumps(c3),json.dumps(c4),
                        ts2 + 'node2,node3,node1-5002,node1-6004', json.dumps(c5), json.dumps(c6),json.dumps(c7), json.dumps(c8),str1])

# schedule.every().day.at("05:00").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
job()