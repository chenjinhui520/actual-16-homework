# coding=utf-8
nums=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
n1=0
n2=0
n3=0
n4=0
# if 语句
for x in nums:
    if n1>x:
        n1=n1
    else:
        n1=x
    maxNum = n1
        
print 'if语句得到最大的数是%s' %(maxNum)
for x in nums:
    if n2>x:
        n2=n2
    else:
        n2=x
    if n2==maxNum:
        continue
    secondMaxNum =n2
print 'if语句得到第二大的数是%s' %(secondMaxNum)

#while 语句
for x in nums:
    while n3<x:
        n3=x
        maxNum=n3

print 'while语句得到最大的数是%s' %(maxNum)
for x in nums:
    while n4 < x:
        n4 = x
        if n4 == maxNum:
            continue
        secondMaxNum=x
print 'while语句得到第二大的数是%s' %(secondMaxNum)








