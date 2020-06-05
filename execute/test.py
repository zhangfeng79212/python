import sys
import fabric
dicts=[
{"ip": "192.168.14.141", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "192.168.14.141", "username": "ms", "password": "cintel1234!@#$", "port": "22"}

]
command=sys.argv[1]
for dict in dicts:
    conn = fabric.Connection(dict['ip'], user=dict['username'], port=dict['port'], config=None,
                             connect_kwargs={"password": dict['password']})
    # 判断根分区的空间使用情况
    print("*"*50)
    print("在服务器："+dict['ip']+"运行命令："+command)
    result = conn.run(command=command, warn=True)
    number = result.stdout.strip()
