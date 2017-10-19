
# exam 1
fd = open(filename, 'r')
data1 = fd.read()

data2 = fd.readline()

data3 = fd.readlines()

for line in fd:
    print line

fd.close()


# exam 2
with open(filename, 'r') as fd:
    for line in fd:
        print line


# exam 3
try:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass


# swith
