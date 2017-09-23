#/usr/bin/env python
#coding:utf-8

# 变量
ret = []
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
        ret.append(cmd)
        for x in range(len(ret)):
            print x+1, ret[x]
    elif cmd == 'help':
        print docstring
    else:
        print "命令执行成功:<%s>" % cmd 
        ret.append(cmd)
        

