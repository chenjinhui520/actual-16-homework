#coding: utf-8

'''
lista = ['c','c++','java','php','python','javascript','c','golang','java']
要求：计算lista的每个元素出现的次数

{
    'c' : 2,
    'c++' : 5,
    'java' : 1,
}

'''


newarr = {} 
arr = ['c','c++','java','php','python','javascript','c','golang','java']

'''
for x in arr:

    # 不存在 创建key
    if x not in newarr:
        newarr[x] = 1
    else:
        # 存在 +1
        newarr[x] += 1 
        #counter = newarr[x]
        #newarr[x] = counter + 1
    
print newarr
'''


for x in arr:
    newarr[x] = newarr.get(x, 0) + 1
print newarr
