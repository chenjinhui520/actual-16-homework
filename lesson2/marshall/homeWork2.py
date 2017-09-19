#/usr/bin/env python
#coding=utf-8
help_message = '''1.不停的提示输入，如果输入quit exit q 退出。
2.如果输入命令，则打印命令执行成功。
3.输入history，显示要求和history命令一模一样。
4.输入help，显示帮助信息。 '''
command_history = []
while True:
    command = raw_input("marshallzhangdeMacBook-Pro:~ marshall.zhang$")
    if command in ('quit','exit','q'):
        print "您已退出"
        break
    elif command == 'help':
        command_history.append(command)
        print help_message
    elif command == 'history':
        command_history.append(command)
        for i in range(1,(len(command_history)+1)):
            print ("%s %s"%(i,command_history[i-1]))
    else:
        command_history.append(command)
        print('%s 命令执行成功'%(command))
