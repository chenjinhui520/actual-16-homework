

filename = '/tmp/run_v3.py'

try:
    f = open(filename, 'r')
except IOError as e:
    print 'cannot open', e.args
except Exception as e:
    print e.args
else:
    print f.readline() 
finally:
    print locals()
    if 'f' in locals():
        print 'close'
        f.close()
