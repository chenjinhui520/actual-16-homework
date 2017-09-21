#!/usr/bin/env python
#encoding:utf-8

### 作业1 ###
'''
输入一系列的整数，输入0表示输入结束
排序输出（升序）
'''
num_list = []
while True:
    input=int(raw_input('please input a num: '))
    num_list.append(input)
    num_list.sort()
    print num_list
    if input == 0:
        break

