#coding: utf-8


arr = range(1, 21)
print 'arr: ', arr

'''
arr2 
'''
arr1 = []
for x in arr:
    if x % 2 == 1:
        arr1.append(x)

print 'new arr2: ', arr1



arr1 = [ x for x in arr if x % 2 == 1 ]
print 'new arr3: ', arr1
