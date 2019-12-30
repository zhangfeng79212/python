'''
Created on 2018年1月2日

@author: zhangf
'''
import smtplib
import datetime,time
from email.mime.text import MIMEText
from selenium import  webdriver

mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "zhangfeng79212"                  # 用户名
mail_pass = "abc123com"               # 授权密码，非登录密码

sender = 'zhangfeng79212@163.com'    # 发件人邮箱(最好写全, 不然会失败)
receivers = 'zhangfeng@gztashi.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


def sendEmail(content,title):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def testgzdi():
    browser=webdriver.Chrome()
    browser.get('https://desktop.gzdi.com')
    now=datetime.datetime.now()
    try:
        welcome=browser.find_element_by_id('ctl08_loginAgentCdaHeaderText2')
        print(welcome.text)
        
        if welcome.text=='Please log on to continue.':
            print("ok:"+welcome.text)
            title = '成功登陆广州设计院虚拟桌面' 
            content = '成功登陆广州设计院虚拟桌面'+now.strftime("%Y-%m-%d %H:%M:%S")
            sendEmail(content,title)

        else:
            print("出错了")
            title = '失败登陆广州设计院虚拟桌面' 
            content = '失败登陆广州设计院虚拟桌面'+now.strftime("%Y-%m-%d %H:%M:%S")
            sendEmail(content,title)
    except:
        print('error')
        title = '错误登陆广州设计院虚拟桌面' 
        content = '错误登陆广州设计院虚拟桌面'+now.strftime("%Y-%m-%d %H:%M:%S")
        sendEmail(content,title)
    browser.close()
    browser.quit()    
if __name__ == '__main__':
    while 1<2:
        testgzdi()
        time.sleep(300)
    pass