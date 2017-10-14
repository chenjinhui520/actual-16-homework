

name = ['monkey1', 'xiaoming', 'reboot']
age = [18, 19, 20]
weight = [178, 181, 167]

'''
->
[('monkey1', 18, 178), ('xiaoming', 19, 181), ('reboot', 20, 167)]
'''

# version 1
'''
l1, l2, l3 = [], [], []

for x in [name, age, weight]:
    print x[0]
    print x[1]
    print x[2]
    print '-----------'
    #l1.append(x[0])
    #l2.append(x[1])
    #l3.append(x[2])

#print [tuple(l1), tuple(l2), tuple(l3)]
'''

# version 2
print zip(name, age, weight)
print [(name[0], age[0], weight[0]), (name[1], age[1], weight[1]), (name[2], age[2], weight[2])]


# version 3
print 'map version3 : \n', map(lambda x, y, z:(x, y, z), name, age, weight)

