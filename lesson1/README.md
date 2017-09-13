# 作业 
> 尽量周五下班前把作业提交到Github上
- 一个序列[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]; 求这个list的最大的两个值.

# 附加题
```
'''
猜数游戏
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了
'''

#!/usr/bin/env python
#coding:utf8
import random

x = int(random.random()*100)
i = 0
c = 6

while i < c:
    num = input("Please input a number: ")
    if num > x:
        print "大了"
    elif num < x:
        print "小了"
    else:
        print "猜对了"
        break
    i += 1
```

```

```

# 预习下次课程

- 列表
- 元组
- 字符串
