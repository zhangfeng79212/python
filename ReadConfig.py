import configparser
cf=configparser.ConfigParser()
cf.read("config.ini")
print(cf.options("server"))
print(cf.get("server","host"))
print(cf.get("server","port"))
print(cf.get("server","user"))
print(cf.get("server","password"))
