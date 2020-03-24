#根据callid获取录音，适用于第二第三节点
#首先从calloout表获取地址信息，调用接口下载，然后从callin表里面获取地址信息，调用接口下载
import json
import requests
callid="C20200317184545AC11001402456117"
ip='47.93.23.227'
url1='http://'+ip+':14502'
#获取srfmsgid和ms
header={'Content-Type': 'text/plain;charset=UTF-8'}
header2={'Content-Type':'application/download'}
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
    str1=k.get('srfmsgid')
    print(str1)
    str2=k.get('msserver')
    agentid=k.get('agentid')
    vccid=agentid[6:12]
    print(vccid)
    if(str1 and str2 ):
        print("http://47.93.23.227:8068/cincc-serv/media/download?msServer=media&filepath="+vccid+"/"+str1)
        r1=requests.post("http://47.93.23.227:8068/cincc-serv/media/download?msServer=media&filepath="+vccid+"/"+str1,\
                 headers=header2)
        print(header2)
        print(r1)

#http://47.93.23.227:8068/cincc-serv/media/download?msServer=media&filepath=100009/ccrecord/20200317/9000A13522085163C20200317184432AC11001403537005S20200317184432155205AC11001403537098.mp3
#http://10.30.1.153:8068/cincc-serv/media/download?msServer=ms15&filePath=666666/servicerecord/000001666666006004/20200323/20005A18826438981C202003232226560A1E011626002945S202003232227060624920A1E011603005393.mp3
#获取录音文件
