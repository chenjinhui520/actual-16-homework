## 作业1
```
需求：用户注册和用户登陆
实现：
1. 仿照Github(https://github.com)登陆和注册用户。
2. 注册用户填写注册信息，注册完成，提示用户注册成功。
3. 登陆输入用户名和密码，验证成功，提示用户登陆成功信息；
   验证失败，提示错误的用户名和密码；
   连续输入错误3次，锁定用户，该用户不能在继续输入退出；

注意：
本次作业不需要写入到文件.
```


## 作业2
```
需求: 处理NGINX ACCESS日志
实现：
1. 统计一个日志文件中不同状态码出现的次数；
2. 统计一个日志文件中不同IP出现的次数；
3. 统计同一个ip访问不同一个url的次数；

# 方式1
{
    '80.82.78.38 http://www.baidu.com/cache/global/img/gs.gif' : 2,
    '80.82.78.38 http://www.qq.com/404/search_children.js' : 5,
    '80.82.78.100 http://www.baidu.com/cache/global/img/gs.gif' : 20,
}

# 方式2
> 添加 m['80.82.78.38']['http://www.reboot.com'] = 1 如果不存在就修改
{
    '80.82.78.38' : {
              'http://www.baidu.com/cache/global/img/gs.gif' : 2,
              'http://www.qq.com/404/search_children.js' : 5,
               },
    '80.82.78.100' : {
              'http://www.baidu.com/cache/global/img/gs.gif' : 20,
               },
}

提示：
方式1是必须要实现的；
方式2可选 难度要比方式1上升一个level.
```


## 作业3
```
理解冒泡排序，不看上课代码，手写冒泡排序。
业余时间充分的可以参考这篇算法文章(http://python.jobbole.com/82270/)
```
