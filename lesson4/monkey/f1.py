
# 无参数 无返回值
def func1():
    print "hello world!"

# 无参数 有返回值
def func2():
    print "hello world!"
    return "hw"

# 有参数 有返回值
# 位置参数
def func3(x, y):
    return x + y

# 有参数 有返回值
# 位置参数
def func4(x, y):
    return y, x

# 位置参数 默认参数
def func5(x, y=1):
    print x
    print y

# 位置参数 关键字参数
def func(*args, **kwargs):
    print args
    print kwargs

def func6(x, y, *args, **kwargs):
    print 'x, y is:',x, y
    print 'args is',args
    print "kwargs is",kwargs

func6(12, 34, 45, 67, name='alen', age=23)

# 参数传递
def func7(*args):
    print args

p = (1,2,3, 4,5)
func7(p)
func7(*p)



