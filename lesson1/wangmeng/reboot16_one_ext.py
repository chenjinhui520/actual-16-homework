#！/usr/bin/env python
# -*- encoding:utf-8 -*-

#例题：猜数游戏
#1、猜一个100以内的整数
#2、6次机会
#3、每次猜时，猜对了，显示大了还是小了
# import random
# x = int(random.random()*100)
# print(x,type(x))
# i = 0
# c = 6
# while i < c:
#     num = input('please input a number:')
#     if int(num) > x:
#         print('too big')
#     elif int(num) < x:
#         print('too low')
#     else:
#         print('right,Yeah!')
#         break
#     i += 1
# 练习：龙城探宝
'''
1、你有4条命，2、通过8关；
3、每一关，有两个洞口，每个洞口有一龙把手。其中一条是善良的，一条是邪恶的。
4、有两种可能：
    1）善良的分给你10个金币
    2）邪恶的吃了你，少了一条命
5、每一关场景描述：
    你看到了两个洞口...
    你选择了左|右洞口
    洞口内伸出了一个恐怖的龙头，它张开巨大的嘴巴，一个深沉的声音发出了：
        你好，我的朋友，给你10个金币，继续下一关吧
        or
        去死吧！贪婪的人类！！！
'''
import random
life = 4
guard = 1
gold = 0
while guard <= 8:
    d = input('请选择洞口（左边|右边[l|r]）：')
    rand = random.randint(1, 2)
    if rand == 1:
        print('你好，我的朋友，给你10个金币，继续下一关吧')
        gold += 10
        print('你目前在第%s关，拥有金币：%s，生命：%s'%(guard,gold,life))
        if guard == 8:
            print('恭喜！闯关成功！')
    else:
        print('去死吧！贪婪的人类！！！')
        life -= 1
        if life == 0:
            print('Game Over!你在第%s关死翘翘了!' % (guard))
            break
        print('你目前在第%s关，拥有金币：%s，生命：%s'%(guard,gold,life))
        if guard == 8:
            print('恭喜！闯关成功！')
    guard += 1



