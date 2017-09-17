#coding: utf-8


arr = [1, 2, 3]
#arr1 = [1, 2, 3, 4, 5]

# version1
'''
arr.append(4)
arr.append(5)
arr.append(6)
print arr
'''
# version2
'''
nums = [4, 5, 6]
for x in nums:
    arr.append(x)

print arr
'''
# version3
'''
nums = [4, 5, 6]
arr += nums
print arr
'''

# version4
nums = [4, 5, 6]
arr.extend(nums)
print arr

