import csv
import os
import codecs
date=20200308

f=codecs.open("test.csv", "w",'utf-8')
writer=csv.writer(f)
writer.writerow([u'机器名字',date])
writer.writerow(['ms1xxxx','456'])
writer.writerow(['ms2xxxx','456'])
writer.writerow(['ms3xxxx','456'])
writer.writerow(['ms4xxxx','456'])
writer.writerow(['ms5xxxx','456'])
writer.writerow(['ms6xxxx','456'])
writer.writerow(['ms7xxxx','456'])
writer.writerow(['ms8xxxx','456'])
writer.writerow(['mstotal','456'])
writer.writerow(['media91','456'])
writer.writerow(['media92','456'])
f.close()
