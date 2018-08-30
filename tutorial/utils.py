# -*- coding: utf-8 -*-
import re


class RedisCollection(object):
    def __init__(self, one_url):
        self.collection_name = one_url

    def get_collection_name(self):
        # name = None
        if self.index_all_urls() is not None:
            name = self.index_all_urls()
        else:
            name = 'publicurls'
        return name

    def index_all_urls(self):
        allurls = ['wooyun', 'freebuf']
        result = None
        for allurl in allurls:
            if re.findall(allurl, self.collection_name):
                result = allurl
                break
        return result
