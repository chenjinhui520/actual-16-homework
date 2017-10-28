

filename = '/tmp/run_v3.py1'

try:
    f = open(filename, 'r')
except MyError as e:
    print e.args
else:
    print f.readline() 
finally:
    print locals()
    if 'f' in locals():
        print 'close'
        f.close()
