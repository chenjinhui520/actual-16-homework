#coding: utf-8
num = []
while True:
	count = int (raw_input('请输入数字:'))
	if count == 0:
		break
	num.append(count)
num.sort()
print num
