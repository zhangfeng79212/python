import sys
import paramiko,sys,os
if(len(sys.argv)!=6):
    print("使用方法是：upload.exe 60.205.178.238 root   abc123.com c:/smp2.log /home/smp.log")
    sys.exit(0)
#args='60.205.178.238' 'root'   'abc123.com'   'c:/smp.log' '/home/smp.log'
ip=sys.argv[1]
username1=sys.argv[2]
password1=sys.argv[3]
remotefile=sys.argv[5]
localfile=sys.argv[4]

try:
    tran = paramiko.Transport((ip, 22))
    tran.connect(username=username1, password=password1)
    sftp = paramiko.SFTPClient.from_transport(tran)
    sftp.put(localfile,remotefile)
    print("upload successful!!")
except Exception as ex:
    print("upload fail!!")
    print(ex)
finally:
    tran.close()