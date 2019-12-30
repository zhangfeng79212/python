import pandas as pd                         #导入pandas包
data = pd.read_csv("server.csv")             #读取csv文件
#print(data['ip'])                                #打印所有文件
#for ip in data['ip']:
#    print(ip)
#for index,row in data.iterrows():#行遍历
#    print(row['ip'])

#print(data.iloc[0]['ip']) 1
#print(data.iloc[0]['username'])2
#print(data.iloc[0]['password'])3
print(data.iloc[0,1])

data.iloc[0,4]='abcd'
print(data.iloc[0,4])
