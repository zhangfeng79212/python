import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='60.205.178.238',port=22,username='root',password='abc123.com')
stdin,stdout,stderr=client.exec_command('ls')
print(stdout.read().decode('utf-8'))
client.close()
