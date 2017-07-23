# encoding=utf-8
from MySQLdb import *

try:
    name = raw_input("请输入用户名：")
    conn = connect(host='localhost',port=3306,user='root',passwd='r&j892806304',db='python3',charset='utf8')
    cursors1 = conn.cursor()

    sql = 'insert into student(name) VALUES (%s)'
    #sql = 'update student set name="李莫愁" where id =7'
    #sql = 'delete from student WHERE id = 7'
    cursors1.execute(sql,[name])


    conn.commit()


    cursors1.close()
    conn.close()


except Exception,e:
    print(e.message)