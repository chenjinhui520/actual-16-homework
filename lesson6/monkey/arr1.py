

list01 = [1,3,3,3,3]
print list01
c = 0
for i in list01:
        if i == 3:
                list01.remove(i)
                c += 1
print 'list01 =',list01
print 'delete count of 3:',c
print list01
