#coding: utf-8

'''
打印10到1的整数，但是不打印5和6.
'''

counter = 10

while counter > 0:
    if counter == 5 or counter == 6:
        counter -= 1
        continue
    print counter
    counter -= 1

