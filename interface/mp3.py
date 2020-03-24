#根据callid获取录音，适用于第二第三节点
#首先从calloout表获取地址信息，调用接口下载，然后从callin表里面获取地址信息，调用接口下载
import json
import requests
callid="C20200317184432AC11001403537005"
ip='47.93.23.227'
url1='http://'+ip+':14502'
#获取srfmsgid和ms
header={'Content-Type': 'text/plain;charset=UTF-8'}
data = json.dumps({
"request":"get_cti_callrecord_callid",
"total": "",
"pagesize": "10",
"pageno": "1",
"agentid": "",
"callid": callid,
"starttime":"20200000000000",
"endtime":"20400318000000"
})
print(data)
r = requests.post("http://47.93.23.227:14502/recordService", headers=header,data=data)
print(r.text)
print(r.json().get('output').get('get_cti_callrecord_callid'))
for k in r.json().get('output').get('get_cti_callrecord_callid'):
    print(k.get('srfmsgid'))
    print(k.get('msserver'))


#获取录音文件
