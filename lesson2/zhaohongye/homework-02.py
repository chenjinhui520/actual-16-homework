#!/usr/bin/env python
#encoding:utf-8

### 作业1 ###
'''
实现history
1、不停的提示输入，如果输入quit eixt q 退出
2、如果输入命令，则打印命令执行成功
3、输入history 显示要求和history命令一模一样
'''
history = []
while True:
    shell = raw_input('请输入命令: ')
    history.append(shell)
    print '命令执行成功!'
    if shell == 'quit' or shell == 'exit' or shell == 'q':
        print '退出成功！'    
        break
    if shell == 'history':
        for i in history:
            print i
