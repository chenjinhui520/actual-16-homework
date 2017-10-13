#!/usr/bin/env python
#coding:utf-8
'''
作业3：
    理解冒泡排序，不看上课代码，手写冒泡排序。  
'''
l = [8,5,1,2,4,77,50,666,999,555,888,17]
for i in range(0,len(l)-1):
    for j in range(0,len(l)-1):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print l
