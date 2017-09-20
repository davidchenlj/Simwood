Simwood添加新款价格专用
#!/use/bin/python
# -*- coding: utf-8 -*-
import re, json
f1=file("new.txt", "r")
line1=f1.readlines()
f1.close()

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
         try:
             return dict.__getitem__(self, item)
         except KeyError:
             value = self[item] = type(self)()
             return value

# 读取最新数据价格
row1={}
for l in line1:
    l=l.strip()
    #print l
    x=re.split("\s+", l)
    row1.setdefault(x[0].upper().replace('\s+', ''), []).append(("%s")% (x[1]))
    print "insert into tb_app_price_list(`outer_sku`,`sell_price`,`buy_price`)VALUES('%s', '%s' ,'%s');" % (x[0].upper(), x[2], x[2])
#!/use/bin/python
# -*- coding: utf-8 -*-
import re, json
# 读取旧价格
f=file("old.txt", "r")
line=f.readlines()
f.close()

# 读取最新数据价格
f1=file("new.txt", "r")
line1=f1.readlines()
f1.close()

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
         try:
             return dict.__getitem__(self, item)
         except KeyError:
             value = self[item] = type(self)()
             return value

# 读取最新数据价格
row1={}
_arr_row1=[]
_arr_row2=[]
for l in line1:
    l=l.strip()
    x=re.split("\s+", l)
    if len(x) == 3:
        row1[x[0].upper()]=x[2]
        _arr_row1.append(x[0].upper())

# 获取旧价格,如果新价格大于旧价格不修改，如果小于修改
row_data={}
row=AutoVivification()
for l in line:
    l=l.strip()
    x=re.split("\s+", l)
    if len(x) == 3:
        row_data.setdefault(x[0].upper(), []).append(("%s")% (x[2]))
        _arr_row2.append(x[0].upper())
        try:
            if int(row1[x[0].upper()]) < int(x[2]):
                print "update tb_app_price_list set buy_price='%s' where outer_sku='%s';" % (row1[x[0].upper()], x[0].upper())
        except Exception as error:
#            print error
            pass

#import json
for r in _arr_row1:
    if r not in _arr_row2:
        print "insert into tb_app_price_list(`outer_sku`,`sell_price`,`buy_price`)VALUES('%s', '%s' ,'%s');" % (r,row1[r], row1[r])

#print json.dumps(row_data,indent=4,ensure_ascii=False)
#for l in row_data:
#    if len(row_data[l]) >= 2:
#        print l,row_data[l]
