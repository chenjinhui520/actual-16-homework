#coding=utf8

userinfo = {}

while 1:
    print ' 请选择1或2或3\n 1 register \n 2 login\n 3 exit'
    action = raw_input('action: ')
    if action == '1':
        print '创建你的用户：'
        username = raw_input('Username: ')
        if not userinfo.has_key(username):  # 用户不存在
            email = raw_input('Email Address: ')
            password = raw_input('Password: ')
            userinfo[username] = {
                'email':email,
                'password':password,
                'errornum':0,
                }
            print '%s 注册成功!' % username
        else:
            print '用户 %s 已存在!' % username
    elif action == '2':
        while 1:
            username = raw_input('Username: ')
            password = raw_input('Password: ')
            if username in userinfo:
                if userinfo[username]['password'] == password:
                    print '欢迎 %s!' % username
                    userinfo[username]['errornum'] = 0 # 登录成功，错误次数清零
                    break
                else:
                    userinfo[username]['errornum'] += 1
                    print 'password error!'
            else:
                print '用户 %s 不存在' % username
                break
            print 'errornum: ', userinfo[username]['errornum']
            if userinfo[username]['errornum'] >= 3:
                print '%s failed 3 times! account locked' % username
                break
    elif action == '3':
        break

    
