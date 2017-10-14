

l = [(3, 2), (1, 9), (2, 8)]

#l.sort(key=lambda x1:x1[1])
#print l


# sorted
new_arr = sorted(l, key=lambda x1:x1[1], reverse=True)
print new_arr

# 对map中的key or value排序
m = {'a': 2, 'b': 100, 'c': 90}
arr1 = sorted(m.items(), key=lambda x:x[1])
