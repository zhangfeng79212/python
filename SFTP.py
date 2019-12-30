import paramiko
tran=paramiko.Transport(('60.205.178.238',22))
tran.connect(username="root",password='abc123.com')
sftp=paramiko.SFTPClient.from_transport(tran)
localpath="d:/SW1.wav"
remotepath="/root/test"
#sftp.get(remotepath, localpath)
#print(sftp.listdir(remotepath))
for filename in sftp.listdir(remotepath):
    print(filename)
tran.close()
