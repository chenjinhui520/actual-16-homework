

l = ['zhengys', 'wshuai', '26', '13260071987']

newl = []
for x in l:
    if x.islower():
        newl.append(x)

print newl
print filter(lambda x:x.islower(), l)
