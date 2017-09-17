#coding: utf-8

s = '''root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
avahi-autoipd:x:170:170:Avahi IPv4LL Stack:/var/lib/avahi-autoipd:/sbin/nologin
systemd-bus-proxy:x:999:997:systemd Bus Proxy:/:/sbin/nologin
systemd-network:x:998:996:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:997:995:User for polkitd:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
liuziping:x:1000:1000::/home/liuziping:/bin/bash
kk:x:1001:1001::/home/kk:/bin/bash
mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash
es:x:1002:1002::/home/es:/bin/bash
nginx:x:996:994:Nginx web server:/var/lib/nginx:/sbin/nologin
woniu:x:1003:1003::/home/woniu:/bin/bash
raopeng:x:1004:1004::/home/raopeng:/bin/bash
sunfan:x:1005:1005::/home/sunfan:/bin/bash
rongjunfeng:x:1006:1006::/home/rongjunfeng:/bin/bash
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
zabbix:x:995:993:Zabbix Monitoring System:/var/lib/zabbix:/sbin/nologin
smbuser:x:1007:1007::/home/smbuser:/bin/bash
leon:x:1008:1008::/home/leon:/bin/bash
jenkins:x:994:992:Jenkins Automation Server:/var/lib/jenkins:/bin/false
gitlab-www:x:993:991::/var/opt/gitlab/nginx:/bin/false
git:x:992:990::/var/opt/gitlab:/bin/sh
gitlab-redis:x:991:989::/var/opt/gitlab/redis:/bin/false
gitlab-psql:x:990:988::/var/opt/gitlab/postgresql:/bin/sh
bingan:x:1009:1009::/home/bingan:/bin/bash
redis:x:989:983:Redis Database Server:/var/lib/redis:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
duguiyang:x:1010:1010::/home/duguiyang:/bin/bash
panweihan:x:1011:1011::/home/panweihan:/bin/bash
niushaoshuai:x:1012:1012::/home/niushaoshuai:/bin/bash
tudou:x:1013:1013::/home/tudou:/bin/bash
liuyang:x:1014:1014::/home/liuyang:/bin/bash
yangyi:x:1015:1015::/home/yangyi:/bin/bash
zhengyscn:x:1016:1016::/home/zhengyscn:/bin/bash'''

arr = list(s)

# 统计\n出现的次数

# 要求2种实现方式

# version1 list.count
count = arr.count('\n')
print count 

# version for x in list:
counter = 0
for x in arr:
    if x == '\n':
        counter += 1
print counter


