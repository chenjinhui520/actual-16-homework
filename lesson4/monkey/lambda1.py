
'''
def f1(x, y):
    return x + y

s = f1(2, 3)
print s


f2 = lambda x, y:x + y
print f2(2, 3)
'''

def f3(x):
    return x[1]

l = [(1, 2), (5, 1), (4, 3)]

# v1
l.sort(key=f3)
print l

# v2
l.sort(key=lambda x:x[1])


def f4(x):
    return x * 2
