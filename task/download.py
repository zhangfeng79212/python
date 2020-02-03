import sys
import paramiko,sys,os
if(len(sys.argv)!=6):
    print("使用方法是：download.exe 60.205.178.238 root   abc123.com  /home/smp.log c:/smp2.log")
    sys.exit(0)
#args='60.205.178.238' 'root'   'abc123.com'  '/home/smp.log' 'c:/smp.log'
ip=sys.argv[1]
username1=sys.argv[2]
password1=sys.argv[3]
remotefile=sys.argv[4]
localfile=sys.argv[5]

try:
    tran = paramiko.Transport((ip, 22))
    tran.connect(username=username1, password=password1)
    sftp = paramiko.SFTPClient.from_transport(tran)
    sftp.get(remotefile, localfile)
    print("download successful!!")
except Exception as ex:
    print("download fail!!")
    print(ex)
finally:
    tran.close()