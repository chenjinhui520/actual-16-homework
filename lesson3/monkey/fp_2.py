#coding: utf-8

# 1. 打开一个文件
fd = open('monkey.txt', 'w')

# 2. 操作文件
'''必须是字符串类型 否则异常报错'''
fd.write('123\n')
fd.write('\n')
fd.write('456')
fd.write(str(100))

# 3. 关闭文件
fd.close()
