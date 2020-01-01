import pandas as pd
import paramiko
data = pd.read_csv("server.csv")             #读取csv文件

for index,row in data.iterrows():
    print('start connect')
    print(row['ip'])
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=row['ip'],port=22,username=row['username'],password=row['password'])
        stdin, stdout, stderr = client.exec_command('/home/setup/lickey cintel')
    except:
        client.close()
        continue
    str=stdout.read().decode('utf-8')
    print(row['ip'])
    print(str)
    data.loc[index,4]=str

data.to_csv('server2.csv')
#client.close()