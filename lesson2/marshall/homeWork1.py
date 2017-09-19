#/usr/bin/env python
#coding=utf-8
help_message = "输入一系列的整数，输入0 表示输入结束"
mylist = []
while True:
    number = raw_input("请输入一个整数：")
    try:
        number = int(number)
    except ValueError:
        print('您输入的不是整数，请输入一个整数')
        continue
    else:
        mylist.append(number)
    if number == 0 :
        break
mylist.sort()
print mylist
