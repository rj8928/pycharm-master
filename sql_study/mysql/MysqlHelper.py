# coding=utf-8
from MySQLdb import *

class MysqlHelper:
    def __init__(self,host,port,db,user,passwd,charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # 增删改
    def cud(self,sql,params):
        try:
            # 连接数据库
            self.open()

            self.cursor.execute(sql,params)
            # 提交事务
            self.conn.commit()

            # 关闭数据库连接
            self.close()

        except Exception,e:
            print (e.message)

        # 查询
    def all(self,sql,params):
        try:
            self.open()

            self.cursor.execute(sql, params)
            #self.conn.commit()
            result = self.cursor.fetchall()

            self.close()
            return result

        except Exception, e:
            print (e.message)

    def one(self, sql, params):
        try:
            self.open()

            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()

            self.close()
            return result

        except Exception, e:
            print (e.message)