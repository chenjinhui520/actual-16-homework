import json


# wirte
fp = open('file.db', 'w')
json.dump(range(1, 10, 1), fp)
fp.close()


# load
fp = open('file.db', 'r')
data = json.load(fp)
print data
fp.close()
