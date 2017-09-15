#!/usr/bin/env python
#edcoding:utf-8

import random
life = 4
count = 1
money = 0
while count < 9:
    name = raw_input('please input your choses : ')
    if random.random() >= 0.5:
        i = 'left'
    elif random.random() < 0.5:
        i = 'right'
    if life <= 0:
        break
    if name == i:
        money -= 10
        life -= 1
        print '去死吧！！贪婪的人类！！'
    elif name != i:
        count += 1
        money += 10
        print '你好，我的朋友，给你10金币，继续下一关吧！'
    print '冒险者，你还有 %s 条命，还有 %s 个金币,八个关卡已闯关 %s 个' % (life,money,count)
print '杀你祭天！'
    


