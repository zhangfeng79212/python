import easygui as g
import paramiko
import os
msg = "请填写要下载的callid"
title = "呼叫中心下载"
fieldNames = ["*callid","下载地址(选填)"]
fieldValues = ['C201912261525340A1E021500402288','d:']
fieldValues = g.multenterbox(msg,title,fieldNames)
#print(fieldValues)
#fieldValues = ['C201912261525340A1E021500402288','c:']
print(fieldValues)


tran=paramiko.Transport(('10.30.2.81',22))
tran.connect(username="lamp",password='cintel1234!@#$')
sftp=paramiko.SFTPClient.from_transport(tran)
str=fieldValues[0]
path1=str[1:9]
path2=str[9:11]
path3=str[11:13]
path4=str[13:15]
path_acd='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/acd1.log'
path_cti='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/cti1.log'
local_acd='c:/'+str+'/acd1.log'
local_cti='c:/'+str+'/cti1.log'
local_path='c:/'+str
if not os.path.exists(local_path):
    os.mkdir('c:/'+str)
print(path_acd)
print(path_cti)
print(local_acd)
print(local_cti)
try:
    sftp.get(path_acd, local_acd)
    sftp.get(path_cti, local_cti)
except:
    pass
#print(sftp.listdir(remotepath))
#for filename in sftp.listdir(remotepath):
#    print(filename)
tran.close()

tran=paramiko.Transport(('10.30.3.81',22))
tran.connect(username="lamp",password='cintel1234!@#$')
sftp=paramiko.SFTPClient.from_transport(tran)
str=fieldValues[0]
path1=str[1:9]
path2=str[9:11]
path3=str[11:13]
path4=str[13:15]
path_acd='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/acd1.log'
path_cti='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/cti1.log'
local_acd='c:/'+str+'/acd1.log'
local_cti='c:/'+str+'/cti1.log'
local_path='c:/'+str
if not os.path.exists(local_path):
    os.mkdir('c:/'+str)
print(path_acd)
print(path_cti)
print(local_acd)
print(local_cti)
try:
    sftp.get(path_acd, local_acd)
    sftp.get(path_cti, local_cti)
except:
    pass
#print(sftp.listdir(remotepath))
#for filename in sftp.listdir(remotepath):
#    print(filename)
tran.close()