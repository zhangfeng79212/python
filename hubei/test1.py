import pandas as pd
import paramiko
data = pd.read_csv("ipaddr.csv")
#读取csv文件
'''
for index,row in data.iterrows():
    if row['name']=="tts":
        print(str(index)+":"+row['ip'])
'''
df=data[data.name=="ivrinterface"]
#print(df.loc[:,['ip']])
#for i in {70..77} {86..91} {190..197} {206..211};do echo `ssh 10.25.58.$i "grep \"13659872144\" /data/ivrInterface/tomcat*/logs/catalina.out.2020-01-02|grep \"流量套餐办理\""`
#通过时间，电话号码，办理的业务，查出业务办理失败的原因
date="2020-01-02"
telephone="13659872144"
busi="流量套餐办理"
command="for i in {70..77} {86..91} {190..197} {206..211};"\
      "do echo $i:`ssh 10.25.58.$i \"grep "+ telephone +" /data/ivrInterface/tomcat*/logs/catalina.out."+date+"|grep "+busi+"\"`;done"
print(command)
#我们就是想看一下最后14:59这一通电话的交互记录，就比如说按了什么键触发了什么引导语播报，12月31日，15002772097
