#/usr/bin/env python
#coding:utf-8

import os

l = []


'''
while True:
    con = raw_input('please input command:')
    if con == 'quit' or con == 'exit' or con == 'q':
        print 'quit'
        break
    elif con == 'history':
        l.append(con)
        for i in l:
            print "%s %s" %(l.index(i)+1,i)
    elif con == 'help':
        print os.system(con)
    else:
        print "命令执行成功:<%s>" % con
        l.append(con)
'''

# 变量
ret = []
counter = 1
exit_cmds =('quit', 'exit', 'q')

docstring = '''
    quit | exit | q  : 退出交互式环境
    history          : 打印历史命令
    help             ：查看帮助信息
'''

# 逻辑
while True:
    cmd = raw_input('please input command: ')
    if cmd in exit_cmds:
        print 'quit'
        break
    elif cmd == 'history':
        ret.append('%s %s' % (counter, cmd))
        counter += 1
        for x in ret:
            print x
    elif cmd == 'help':
        print docstring
    else:
        print "命令执行成功:<%s>" % cmd 
        ret.append('%s %s' % (counter, cmd))
        counter += 1
        

