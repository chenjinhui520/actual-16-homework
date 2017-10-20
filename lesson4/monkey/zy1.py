#coding: utf-8


counter = 0
max_retry_counter = 3
personinfos = []


while True:

    action = raw_input('\nPlease input your action: ')

    if action == 'register':
        print '\n\tCreate your personal account\n'
        username = raw_input('Username: ')
        email = raw_input('Email Address: ')
        password = raw_input('Password: ')

        #1. 检查该注册的新用户是否存在，如果存在就不在注册。
        usernames = [ x['username'] for x in personinfos if x ]
        if username in usernames:
            print "username:%s already exists." % username
            continue

        registerInfo = {'username' : username, 'email' : email, 'password' : password}
        personinfos.append(registerInfo)
        print 'account %s is created sucess' % username

    elif action == 'login':
        if counter >= max_retry_counter:
            print "bad username or password more than 3, exception exit."
            break

        username = raw_input('Username: ')
        password = raw_input('Password: ')

        # 1. 判断用户是否存在
        usernames = [ x['username'] for x in personinfos if x ]
        if not usernames or username not in usernames:
            print 'username:%s not found, please register your account.' % username
            continue

        # 2. 用户存在，判断用户对应的密码是否正确
        map_user_pass_dic = { x['username'] : x['password'] for x in personinfos if x }
        if map_user_pass_dic.get(username) == password:
            print "Username %s login sucess." % username
            print '''
                    Welcome to reboot actual 16.
            '''
        else:
            print 'bad username or password'
            counter += 1

    elif action == 'quit':
        print "layout sucess."
        break

    else:
        print "action is required, please choice ['resiger', 'login', 'quit']."


print "Game Over."
print personinfos
