#根据callid获取录音，适用于第二第三节点
#首先从calloout表获取地址信息，调用接口下载，然后从callin表里面获取地址信息，调用接口下载
import json
import requests
import easygui as g
msg = "请填写要下载的callid"
title = "呼叫中心下载"
fieldNames = ["*callid"]
fieldValues = ['C20200309153040C0A80E8D03361206']
fieldValues = g.multenterbox(msg,title,fieldNames)

requests.adapters.DEFAULT_RETRIES = 15
s = requests.session()
# 设置连接活跃状态为False
s.keep_alive = False
callid=fieldValues[0]

def downloadmp3(callid,ip):
    url1='http://'+ip+':14502/recordService'
    starttime=callid[1:7]+"01000000"
    endtime=callid[1:7]+"32000000"
    #获取srfmsgid和ms
    header={'Content-Type': 'text/plain;charset=UTF-8','Connection': 'close'}
    data = json.dumps({
    "request":"get_cti_callrecord_callid",
    "total": "",
    "pagesize": "10",
    "pageno": "1",
    "agentid": "",
    "callid": callid,
    "starttime":starttime,
    "endtime":endtime
    })
    try:
        r=s.post(url1, headers=header,data=data,stream=False,timeout= 10)
        print(ip,r)
        if(r.json().get('output').get('get_cti_callrecord_callid')):
            for k in r.json().get('output').get('get_cti_callrecord_callid'):
                srfmsgid=k.get('srfmsgid')
                filename=srfmsgid.split('/')[-1]
                msserver=k.get('msserver')
                agentid=k.get('agentid')
                vccid=agentid[6:12]
                print("----------------",vccid,msserver,filename)
                if(msserver and srfmsgid ):
                    down_url = "http://"+ip+":8068/cincc-serv/media/download"
                    down_data = {"msServer": msserver,
                                 "filePath": vccid+"/"+srfmsgid,
                                 }
                    print(down_url)
                    print(down_data)
                    down_res = s.get(url=down_url, params=down_data)

                    with open(filename, "wb") as code:
                        code.write(down_res.content)
                        #下面是下载cca
                    filename1=filename[:-4]+"CCA.wav"
                    down_data = {"msServer": msserver,
                                 "filePath": vccid + "/" + srfmsgid[:-4]+"CCA.wav",
                                 }
                    print(down_url)
                    print(down_data)
                    down_res = s.get(url=down_url, params=down_data)

                    with open(filename1, "wb") as code:
                        code.write(down_res.content)
                        # 下面是下载ccb
                    filename2 = filename[:-4] + "CCB.wav"
                    down_data = {"msServer": msserver,
                                 "filePath": vccid + "/" + srfmsgid[:-4]+"CCB.wav",
                                 }
                    print(down_url)
                    print(down_data)
                    down_res = s.get(url=down_url, params=down_data)

                    with open(filename2, "wb") as code:
                        code.write(down_res.content)
    except Exception as ex:
        print("execute fail!!")
        print(ex)
    finally:
        s.close()


downloadmp3(callid,'10.30.1.153')
downloadmp3(callid,'10.30.2.153')
downloadmp3(callid,'10.30.3.153')
downloadmp3(callid,'192.168.14.141')