#coding: utf-8

arr = ['python', 'golang', 'java', 'c']
#print type(arr)
print 'arr: ', arr

arr1 = ['js', 'vue']
arr[2:2] = arr1 
print 'arr insert: ', arr

####
start = 2
end = 4
arr[start:end] = []
print 'arr4 udpate: ', arr


nums = range(1, 10)
arr[3:3] = nums
print 'arr3 insert: ', arr


arr[2:-2] = []
print 'arr3 udpate: ', arr
