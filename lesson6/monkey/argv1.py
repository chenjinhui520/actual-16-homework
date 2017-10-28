

import sys


print sys.argv


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
    output += 'line'    

    output = '''\
    1 /etc/passwd
    2 df -h
    3 123
    '''
    return output
argv = sys.argv
#argv = sys.argv[1:]
result = funcArgv(argv)
print result



'''
函数名字 execute_command
函数接收一个参数，这个参数是执行脚本传递过来的参数
参数 'df -h' 'free -m' 'disk'

# python argv.py 'df -h' 'free -m' 'disk'
command: df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        40G  6.2G   32G  17% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
/dev/vdb         99G   60M   94G   1% /data

command: free -m
             total       used       free     shared    buffers     cached
Mem:          7872       4569       3303          0        446       3212
-/+ buffers/cache:        910       6962
Swap:            0          0          0
'''
