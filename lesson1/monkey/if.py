#coding: utf-8

'''
name = raw_input('please input your name: ')
if name == 'monkey':
    print 'ok'
'''

'''
# 语句块中的缩进要保持一致
if False:
    print 'ok1'
    print 'ok2'
    print 'ok4'
else:
    print 'ok3'
'''

name = raw_input('please input your name: ')
if name == 'monkey':
    print 'ok'
elif name == 'kk':
    print 'kk ok'
    print 'kk ok1'
    print 'kk ok2'
    print 2 + 3
else:
    print 'err'

print 'Over'
