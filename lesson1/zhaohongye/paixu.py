#!/usr/bin/env python
#encoding:utf-8
#author:zhy
#data:2017-9-15
num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num = 0
max2_num = 0
for i in num_list:
    if i > max_num:
        max_num = i
for i in num_list:
    if i > max2_num and i < max_num:
        max2_num = i
print '此列表中最大的值为%s,第二大的值为%s ' % (max_num,max2_num)
