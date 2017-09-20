#!/usr/bin/env python
#coding=utf-8 

import os

cmd = []
while 1:
    temp_cmd = raw_input("请输入命令: ")
    ex = ['quit','exit','q']
    if temp_cmd in ex:
        break
        
    elif temp_cmd == 'help':

        cmd.append(temp_cmd)
        print '这里是帮助信息 输入exit quit q可以退出 输入history获取历史记录 输入其他命令得到返回结果'
        
    elif temp_cmd == 'history':
        cmd.append(temp_cmd)
        print cmd
    
    else:
        cmd.append(temp_cmd)
        val = os.system(temp_cmd)
        print val
