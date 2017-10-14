#coding: utf-8

def f1(x, y, z):
    print x, y, z

# 可变参数
def f2(*args):
    print args

def f3(x, y, *args):
    print x
    print y
    print args 

def f4(**a):
    print a 

def f5(x):
    print x


def f6(x, y, *args, **kwargs):
    print x
    print y 
    print args
    print kwargs

#f1(1, 2, 3, 4, 5)
#f2(1, 2, 3, 4, 5)

#f3(1, 2, 3, 4, 5, 6, 7, 8)

#f4(name='monkey', sex='male')

#m = {'name' : 'monkey', 'sex' : 'male'}
#f4(**m)

#ret = f5(m)
#print type(ret), ret

f6(1, 2, 3, 4, 5, 6, age='18', name='monkey')
