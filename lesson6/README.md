# 作业 

1. 完善用户注册、登录、查看的功能;
2. 登录页面改成使用bootstrap的登录页面；
3. 将flask代码和工具函数拆分；

> 模块拆分
```bash
├── common.py       # 工具函数 或 通用函数;
├── flask_web.py    # flask的核心代码;
├── static          # 静态文件，比如css/js/image等;
├── templates       # 静态文件；
└── tests.py        # 测试文件；
```

> 注意
```
标准模块(os/sys)部分多练习
funcArgv 和 execute_command 两个函数不看代码在写一遍
```

## 二维码生成

```python
#coding: utf-8
# pip install Image
# pip install qrcode

import qrcode

# 设置二维码图片绑定的网址
img = qrcode.make('https://github.com/467754239')

# 生成二维码图片
with open('reboot-actual.png', 'wb') as f:
    img.save(f)
```

![二维码](./monkey/reboot-actual.png)
