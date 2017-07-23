# coding=utf-8
from MysqlHelper import MysqlHelper

#name = raw_input("请输入学生姓名")
#id1 = raw_input("请输入学生编号")

sql = 'select * from student WHERE id=%s'
params =[1]

exeslq = MysqlHelper('localhost',3306,'python3','root','r&j892806304')
view = exeslq.all(sql,params)

# 遍历数组
for temp in view:
    for i in temp:
        print ("%s\t"%i),
    print ""
