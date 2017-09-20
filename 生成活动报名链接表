用于淘宝官方活动报名,生成对应的链接，方便报名活动.
#!/usr/bin/python
#-*- coding:utf-8-*-
import re
import shuaishou

dict1={}
for row in shuaishou.dict1['RelatedItems']:
    dict1[row['ProviderItemOnlineKey']]=row['ItemUrl']

hd_price=[]
with open('list.txt') as f:
    for line in f:
        line=line.strip()
        line=re.split('\s+', line)
        if dict1.has_key(line[0]):
            print '{},{},{}'.format(line[1], line[2], dict1[line[0]])
        else:
            print '找不到,{},{},{}'.format(line[0], line[1], line[2])
