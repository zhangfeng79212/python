import easygui as g

msg = "请填写要下载的callid"
title = "呼叫中心下载"
fieldNames = ["*callid","*下载地址"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)
#print(fieldValues)
print(fieldValues)