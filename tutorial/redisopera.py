# -*- coding: utf-8 -*-
import redis
from tutorial.utils import RedisCollection


class RedisOpera:
    def __init__(self, stat):
        self.r = redis.Redis(host='111.231.64.142', port=6379, db=0)

    def write(self, values):
        # print self.r.keys('*')
        collection = RedisCollection(values).get_collection_name()
        self.r.sadd(collection, values)

    def query(self, values):
        collection = RedisCollection(values).get_collection_name()
        return self.r.sismember(collection, values)

