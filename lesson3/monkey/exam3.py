#coding: utf-8

'''
列表
[1, 2, 3, 4, 3, 12, 3, 3, 4, 2, 433, 333, 333, 1, 2]

1. 去重，得到不重复的元素
'''


s = [1, 2, 3, 4, 3, 12, 3, 3, 4, 2, 433, 333, 333, 1, 2]

newret = []

for x in s:
    if x not in newret:
        newret.append(x)

print newret

'''
set 集合 将一个对象转换成集合类型 type
list 列表 将要给对象转换成列表类型 type
'''
print list( set(s) )
