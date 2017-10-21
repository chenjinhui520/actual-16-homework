

num1 = input('number')  # return type -> int
num2 = raw_input('number') # return type -> str

try:
    s = num1 + num2
except Exception as e:
    print 'sum error, info:%s' % e.args
else:
    print s
finally:
    print 'before finish'

print 'finish.'
