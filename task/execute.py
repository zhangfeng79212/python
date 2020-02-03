import sys
import paramiko,sys,os
import time
import threading
if(len(sys.argv)<5):
    print("使用方法是：execute.exe 60.205.178.238 root   abc123.com  \"mysql -ucincc -pcinCC1234 -e 'show databases'\" ")
    sys.exit(0)
#args='60.205.178.238' 'root'   'abc123.com'  '/home/smp.log' 'c:/smp.log'
ip=sys.argv[1]
username1=sys.argv[2]
password1=sys.argv[3]
command1=sys.argv[4]
count1=len(sys.argv)
print(count1)
try:
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip,port=22,username=username1,password=password1)
    chan = client.invoke_shell()

    def writeall(sock):
        while True:
            data = sock.recv(1024)
            if not data:
                sys.stdout.write("\r\n*** EOF ***\r\n\r\n")
                sys.stdout.flush()
                break
            sys.stdout.write(data.decode("utf-8"))
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
    i=4
    while i<count1:
        chan.send(sys.argv[i])
        chan.send('\n')
        i=i+1
        print(i)
    time.sleep(5)
    print("execute successful!!")
except Exception as ex:
    print("execute fail!!")
    print(ex)
finally:
    chan.close()
    client.close()



