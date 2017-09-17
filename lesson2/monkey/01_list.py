#coding: utf-8

import time
'''
去除arr中重复的元素

for in遍历时不要在遍历中删除数据
'''
arr = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]

'''
# 方式1
for x in arr:
    if arr.count(x) > 2:
        arr.remove(x)
print arr

# 方式2
for x in arr:
    while arr.count(x) > 1:
        index = arr.index(x)
        del arr[index]
        print arr
print arr
'''

# 方式3
arr2 = []
for x in arr:
    if x not in arr2:
        arr2.append(x)

print arr2


# 方式4
arr3 = list(set(arr))
print arr3




