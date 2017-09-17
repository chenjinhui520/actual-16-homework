#coding: utf-8

arr = [13, 11, 6, 4, 2, 10]

#max_val = 0
#
#for x in arr:
#    if x > max_val:
#        max_val = x
#
#print max_val

value=9999999
value = arr[0] 
for x in arr:
    if x < value:
        value = x
print value

