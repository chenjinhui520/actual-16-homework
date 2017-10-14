

s = 0
for x in range(1, 11, 1):
    s += x
print s

print 'reduce: ', reduce(lambda x, y: x+y, range(1, 11, 1))
