#coding: utf-8

def f(name, address=None):
    print name
    print address

def f2(**kwargs):
    print kwargs['name']
    print kwargs['address']
    print kwargs['age']


def f3(*args):
    print args

m = {'name' : 'monkey', 'address' : 'bj', 'age' : 27}
#f(**m)
#f(name='monkey', address='bj', age=27)
#f2(name='monkey', address='bj', age=27)

p = range(1, 11)
f3(p)
f3(p, 1, 2)
f3(1, 2, *p)
#f3(1, 2, 1, 2, 3, ...., 10)





