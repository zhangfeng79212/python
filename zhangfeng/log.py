import easygui as g
import paramiko
import os
import time
msg = "请填写要下载的callid"
title = "呼叫中心下载"
fieldNames = ["*callid","下载地址(选填)"]
fieldValues = ['C202001100004110A1E021706720222','d:']
fieldValues = g.multenterbox(msg,title,fieldNames)
#print(fieldValues)
#fieldValues = ['C201912261525340A1E021500402288','c:']
print(fieldValues)
str=fieldValues[0]
path1=str[1:9]
path2=str[9:11]
path3=str[11:13]
path4=str[13:15]
dir_remote='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str
dir_local='c:/'+str
def download(ip,nodeX):
    try:
        tran=paramiko.Transport((ip,22))
        tran.connect(username="lamp",password='cintel1234!@#$')
        sftp=paramiko.SFTPClient.from_transport(tran)
        if not os.path.exists(dir_local):
            os.mkdir('c:/'+str)
        files = sftp.listdir_attr(dir_remote)
        for file in files:
            filename_remote = dir_remote + '/' + file.filename
            filename_local = dir_local + '/' + file.filename
            sftp.get(filename_remote,filename_local)
    except Exception as ex:
        print("第"+nodeX+"节点日志下载错误")
        print(ex)
        pass
    finally:
        tran.close()
download('10.30.2.81','二')
download('10.30.3.81','三')