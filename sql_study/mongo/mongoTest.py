# coding=utf-8

from pymongo import *

# 获取客户端，建立连接            用户名：密码@主机：端口：数据库
client = MongoClient('mongodb://py3:123@localhost:27017/python3')
# 切换数据库
db = client.python3
# 获取集合
stu = db.stu

# 增加
# stu.insert_one({'name':'张三'})

# 修改            where                set
# stu.update_one({'name':'张三'},{'$set':{'name':'abc'}})

# 删除
# stu.delete_one({'name':'abc'})

# 查询                  age大于20
# cursor = stu.find({'age':{'$gt':20}})
# for s in cursor:
#     print (s['name']) 遍历取出名字