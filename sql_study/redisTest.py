# coding=utf8
from redis import *

r = StrictRedis(host='localhost',port=6379)

# # 写
# pipe = r.pipeline()
# pipe.set('python3','redis')
# pipe.set("pyhton4", 'haha')
# pipe.execute()

# 读
# temp = r.get('python3')
# print (temp)


class redisHelper():
    def __init__(self,host, port):
        self.__redis = StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)