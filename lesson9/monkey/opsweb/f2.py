
from functools import wraps


def decorator(f):
    
    @wraps(f)
    def wrapper():
        '''
        decorator of wrapper func
        '''
        f()
    return wrapper

@decorator
def func():
    '''
    do someting
    '''
    print 'hello world.'

func()
print func.__doc__
print func.__name__
