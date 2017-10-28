
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        print x

        #print name

        print 1 / 0
        break
        #if True print 123
    except ValueError as e:
        print 'int(x) error' 
    except NameError as e:
        print 'name not define error'
    except Exception as e:
        print 'error1' 
        print "args>>> ", e.args
        print "message>>> ", e.message
        print e.errno
        print dir(e)

print 'end'
