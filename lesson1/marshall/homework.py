#!/usr/bin/env python
#coding=utf-8
'''找到一个列表中最大值和第二最大值'''

nums=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

def findOne(nums):
    max = 0
    second_max = 0
    # 找到最大值
    for num in nums:
        if(num > max):
            max = num
    print("最大值是%s"%(max))
    # 将最大值从列表中忽略 找到第二最大值

    for num in nums:
        if num in nums:
            if(num == max):
                pass
            elif(num > second_max):
                second_max = num
    print("第二最大值是%s"%(second_max))


def findTow(nums):
    # 使用列表冒泡排序找出来最大和第二最大值
    length = len(nums)
    max = nums[0]
    for i in range(length,0,-1):
        for j in range(i-1):
            if nums[j] > nums[j+1] :
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print("最大值是%s,第二最大值是%s"%(nums[-1],nums[-2]))

def findTree(nums):
    # 使用选择排序找出最大值和第二最大值
    length = len(nums)
    for j in range(length-1):
        min_id = j
        min = nums[j]
        for i in range(j,length):
            if nums[i] < min:
                min_id = i
                min = nums[i]
        nums[j],nums[min_id] = nums[min_id],nums[j]
    print(nums)
def findFour(nums):
    # 找到最大值然后把它从列表中pop出去，然后再从列表中找到最大值
    length = len(nums)
    for j in range(length):
        max = nums[0]
        max_id = 0
        for i in range(length-j):
            if nums[i] > max:
                max_id = i

                max = nums[i]
        max_now = nums.pop(max_id)
        print("第%s最大值为%s"%(j+1,max))
findOne(nums)
findTow(nums)
findTree(nums)
findFour(nums)