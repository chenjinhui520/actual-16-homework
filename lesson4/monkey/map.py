#coding: utf-8


'''
1、首先生成三个互有关系的列表
name = ['monkey','pops','join']
age = [27, 19, 28]
weight = [178,165,190]

2、将以上三个列表合并成以下这种列表格式
[(allentuns,25,178),(pops,19,165),(join,28,190)]
'''

name = ['monkey','pops','join']
age = [27, 19, 28]
weight = [178,165,190]

# version 1
# 通过for循环遍历的方式实现
l1, l2, l3 = [], [], []
for x in [name, age, weight]:
    l1.append(x[0])
    l2.append(x[1])
    l3.append(x[2])
result1 = [tuple(l1), tuple(l2), tuple(l3)]
print 'result1: ', result1


# version 2
result2 = zip(name, age, weight)
print 'result2: ', result2


# version 3
def f(name, age, weight):
    return (name, age, weight)
result3 = map(f, name, age, weight)
print 'result3: ', result3
