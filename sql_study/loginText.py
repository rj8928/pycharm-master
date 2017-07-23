# coding=utf8


from redisTest import redisHelper
from MysqlHelper import MysqlHelper
from  hashlib import sha1


# 接收输入
name = raw_input("请输入用户名:")
pwd1 = raw_input("请输入密码:")

# 加密
s1 = sha1()
s1.update(pwd1)
pwd2 = s1.hexdigest()

# 查询redis中是否存在此用户
r = redisHelper('localhost', 6379)
m = MysqlHelper('localhost', 3306, 'python3', 'root', 'r&j892806304')
if r.get(name) == None:
    sql = 'select passwd from users where name=%s'
    pwd3 = m.one(sql, [name])
    if pwd3 == None:
        print ('用户名错误')
    else:
        r.set(name, pwd3[0])
        if pwd3[0] == pwd2:
            print ('登录成功')
        else:
            print ("密码错误")
else:
    if r.get(name) == pwd2:
        print ('登录成功')
    else:
        print ('密码错误')

