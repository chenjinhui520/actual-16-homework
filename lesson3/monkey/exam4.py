#coding: utf-8

'''
[10, 2, 14, 15, 9, 12, 111, 23, 144]
'''

'''
l.sort()
'''

#l = [10, 2, 14, 15, 9, 12, 111, 23, 144]
#l.sort()
#print l


'''
冒泡排序
'''

l = [10, 2, 14, 15, 9, 12, 111, 23, 144]

counter = 1
# range(len(l)) -> 0,.....8
for i in range(1, len(l)):
    for j in range(i):
        print i, j
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
        counter += 1
print counter
print l
