#coding: utf-8

arr = range(0, 11, 1)
'''
1. return list
2. [0, 2, 4, 6, 8, 10]
'''

def f_event_number(arr):

    ''' 逻辑代码
    '''
    #ret = []
    #for x in arr:
    #    if x % 2 == 0:
    #        ret.append(x)
    #return ret 

    # 列表生成式
    return [ x for x in arr if x % 2 == 0 ]


newarr = f_event_number(arr)
print newarr
