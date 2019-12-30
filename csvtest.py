import pandas as pd                         #导入pandas包
data = pd.read_csv("server.csv")             #读取csv文件
#print(data['ip'])                                #打印所有文件
#for ip in data['ip']:
#    print(ip)
for index,row in data.iterrows():#行遍历
    print(row['ip'])

