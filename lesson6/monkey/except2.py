
try:
    fd = open('filename', 'r')
except IOError as e:
    print dir(e)
    print "errno> ", e.errno
    print "strerror> ", e.strerror
    print e



import sys

try:
    f = open('myfile.txt')
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
else:
    s = f.readline()
    i = int(s.strip())
finally:
    if 'f' in locals():
        f.close()
