# -*- coding:utf-8 -*-

a = {}
aa = []

b = {}
bb = []

c = 0
onlyinb=[]
onlyina=[]
for i in b.keys():
    if i not in a.keys():
        print(i)
        c += 1
        onlyb.append(i)
        
print(c)
print('\n**********************\n')
for i in a.keys():
    if i not in b.keys():
        print(i)
        onlya.append(i)
        
# cc = []
# for i in bb:
#     if i not in aa:
#         cc.append(i)
# print(cc)
