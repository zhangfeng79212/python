
str='C201912261525340A1E021500402288'
path1=str[1:9]
path2=str[9:11]
path3=str[11:13]
path4=str[13:15]
path_acd='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/acd1.log'
path_cti='/home/lamp/cin/logs/'+path1+'/'+path2+'/'+path3+'/'+path4+'/'+str+'/cti1.log'
local_acd='d:/'+str+'/acd1.log'
local_cti='d:/'+str+'/cti1.log'
print(path_acd)
print(path_cti)
print(local_acd)
print(local_cti)