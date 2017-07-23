# coding=utf8
from MysqlHelper import MysqlHelper
from hashlib import sha1

name = raw_input("请输入用户名：")
passwd = raw_input("请输入密码:")
i = 1;

while True:
    repasswd = raw_input("请再次输入之前的密码")
    while passwd == repasswd :

        # 加密
        s1=sha1()
        s1.update(passwd)
        pwd = s1.hexdigest()

        # 执行sql语句
        sql = 'insert into users values(0,%s,%s)'
        params = [name,pwd]
        helper = MysqlHelper('localhost',3360,'python3','root','r&j892806304')
        helper.cud(sql,params)

        print ("注册成功")
        i=3 # 跳出双重while
        break

    if i ==3:
        break

    if i ==2:
        print ("注册失败")
        break

    else:
        print ("密码确认错误,请重新输入")
        i +=1


