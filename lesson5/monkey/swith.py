

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def base(num1, num2):
    return (num1 + num2) * 2

'''
while True:
    # action_args > add 1 2
    action_args = raw_input('please input your action and args: ')
    args = action_args.split()
    action, num1, num2 = args[0], int(args[1]), int(args[2])

    if action == 'add':
        ret = add(num1, num2)
    elif action == 'sub':
        ret = sub(num1, num2)
    elif action == 'mul':
        ret = mul(num1, num2)
    elif action == 'div':
        ret = div(num1, num2)
    print ret

'''

while True:
    # action_args > add 1 2
    action_args = raw_input('please input your action and args: ')
    args = action_args.split()
    action, num1, num2 = args[0], int(args[1]), int(args[2])

    actionMap = {'add' : add, 'sub' : sub, 'mul' : mul, 'div' : div, 'base' : base}
    # f = add
    # ret = f(num1, num2)
    ret = actionMap[action](num1, num2)
    print ret
