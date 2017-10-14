


m1 = {'name' : 'monkey', 'age':27, 'address' : 'bj'}

m2 = {}
for k, v in m1.items():
    m2[v] = k
print m2


m3 = { v:k for k, v in m1.items() }
print m3
        

