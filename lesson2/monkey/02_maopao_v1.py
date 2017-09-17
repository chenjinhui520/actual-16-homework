#coding: utf-8

'''
冒泡排序

八大排序算法的
http://python.jobbole.com/82270/

原理
http://blog.csdn.net/fang_fang_2008/article/details/41806635
'''
arr = [10, 2, 14, 115, 9, 12, 111, 23, 144]
print 'start >>> ', arr
for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print 'end >>> ', arr
