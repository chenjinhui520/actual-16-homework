#coding: utf-8

counter = 0 
l = ['python', 'golang', 'java', 'c', 'python', 'golang', 'python']

'''
    统计python出现的次数
for x in l:
    if x == 'python':
        counter += 1

print counter
'''
#l[start:end] 
l[1:1] = ['c++']
print l


arr = [1, 2, 3]
# arr = [1, 2, 3, 4]
arr[3:3] = '4'
print 'new arr: ', arr

