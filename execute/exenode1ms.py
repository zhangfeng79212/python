import sys
import fabric
dicts={
{"ip": "10.30.1.101", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.102", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.103", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.104", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.105", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.106", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.107", "username": "ms", "password": "cintel1234!@#$", "port": "22"},
{"ip": "10.30.1.108", "username": "ms", "password": "cintel1234!@#$", "port": "22"}
}
command=sys.argv[1]
for dict in dicts:
    conn = fabric.Connection(dict['ip'], user=dict['username'], port=dict['port'], config=None,
                             connect_kwargs={"password": dict['password']})
    # 判断根分区的空间使用情况
    result = conn.run(command=command, warn=True)
    number = result.stdout.strip()
    print(number)