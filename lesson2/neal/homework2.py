#coding: utf-8
ari = []
n = 1
while True:
    count = raw_input('请输入命令:')
    if  count in ['quit','exit','q']:
        break
    elif count == 'history':
	for x in ari:
	    print x
    elif count == 'help':
	print '输入quit,exit,q退出，输入history显示历史命令，输入help显示帮助信息'
	ari.append(str(n) + ' ' + count)
	n += 1
    else:
	ari.append(str(n) + ' ' + count)
	n += 1

