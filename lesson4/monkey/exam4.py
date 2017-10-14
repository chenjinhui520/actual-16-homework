
'''
exit_state = True

while True:
     print 'enter'
     if not exit_state:
         break

     for x in range(1, 10, 1):
        if x == 5:
            exit_state = False
            break

print "end"
'''


import sys

while True:
     for x in range(1, 10, 1):
        print x
        if x == 5:
            sys.exit(0) 
