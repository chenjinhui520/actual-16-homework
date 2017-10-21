

arr = []

def f1():
    #global arr
    ret = []
    ret.append(123)
    arr = ret

def f2():
    arr.append(123)

def f3():
    ret = []
    ret.append(123)
    arr = ret
    return arr

f2()
print arr

arr = f3()
print arr
