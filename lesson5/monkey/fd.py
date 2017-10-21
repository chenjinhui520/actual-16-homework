
fd = open(filename, 'r')

# load mem from disk
fd.read()
fd.readlines()

# read line
fd.readline()

fd.close()


with open(filename, 'r') as fd:
    data = fd.read()
    print data


with open(filename, 'r') as fd:
    for line in fd:  # 迭代器
        print line

    '''
    for line in fd.read().split('\n'):
        print line
    '''
