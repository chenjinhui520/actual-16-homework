#coding: utf-8

import os
import sys


#print sys.argv


'''
# python argv.py /etc/passwd 'df -h' 123
1 /etc/passwd
2 df -h
3 123


函数名字叫做 funcArgv
接收一个参数，这个参数就是命令行的所有参数
函数返回\
1 /etc/passwd
2 df -h
3 123
'''


def funcArgv(argv):
    output = ''
    for x in range(len(argv)):
        output = output + "%s %s\n" % (x+1, argv[x])
    output = output.rstrip('\n')
    return output

#result = funcArgv(sys.argv[1:])
#print result

def execute_command(cmds):
    output = ''
    for x in range(len(cmds)):
        command =  cmds[x]
        fd = os.popen( command )
        data = fd.read()
        output = output + "comand: %s \n%s\n" % (cmds[x], data)
    output = output.rstrip('\n')
    return output

result = execute_command(sys.argv[1:])
print result
