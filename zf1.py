import pandas as pd
import paramiko
data = pd.read_csv("server.csv")             #读取csv文件
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for index,row in data.iterrows():
    client.connect(hostname=row['ip'],port=22,username=row['username'],password=row['password'])
    stdin,stdout,stderr=client.exec_command('/home/setup/lickey cintel')
#print(stdout.read().decode('utf-8'))
    str=stdout.read().decode('utf-8')
    print(row['ip'])
    print(str)
    data.loc[index,4]=str
    break
data.to_csv('server2.csv')
#client.close()