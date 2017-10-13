#!/usr/bin/env python
#coding=utf8
def bubble(nums):
    length = len(nums)
    max = nums[0]
    for i in range(length,0,-1):
        for j in range(i-1):
            if nums[j] > nums[j+1] :
                nums[j],nums[j+1] = nums[j+1],nums[j]
    print nums

nums = [2,5,82,1,5,8,0,18]
bubble(nums)
