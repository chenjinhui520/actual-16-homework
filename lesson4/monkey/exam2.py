#coding: utf-8

def f(name, address=None):
    print name
    print address

# 关键字参数
m = {'name' : 'monkey', 'address' : 'bj'}
f(m['name'], m['address'])

print '---'
f(m)

print '---'
f(**m)
f(name='monkey', address='bj')


