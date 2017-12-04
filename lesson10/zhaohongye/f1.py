
'''
from common import ssum

s = ssum(3, 2)
print "f1 ssum: ", s
'''

def helloworld(func):

    def child():
        print "hello world" 
        return func()

    return child 

@helloworld
def func1():
    return 'func version'



handler = helloworld(func1)
print handler()


#print func1()
