#!/usr/bin/env python
# coding: utf-8

nums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_1st = 0
max_2nd = 0

for i in nums:
    if max_1st < i:
        max_2nd = max_1st
        max_1st = i

print "The largest num is: %s" % max_1st
print "The second largest num is: %s" % max_2nd

