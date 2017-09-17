#coding: utf-8

output = ''
counter = 1

while True:
    cmd = raw_input('please input your commmand: ')
    if cmd == 'quit' or cmd == 'exit' or cmd == 'q':
        break
    elif cmd == 'history':
        for x in output.split('\n'):
            print x
    elif cmd == 'help':
        helper = '''
            help            : 查看帮助信息
            quit | exit | q : 退出
            history         : 查看历史命令
            <command>       : 查看历史命令
        '''
        print helper
    else:
        output += '%d %s \n'  % (counter, cmd)
        print 'yes'
    counter += 1

print 'Game Over'
