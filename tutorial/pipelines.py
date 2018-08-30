# -*- coding: utf-8 -*-
from uuid import uuid4
from datetime import datetime
import logging

from tutorial.dbconfig import connection
from tutorial.redisopera import RedisOpera


class CPCPipeline(object):

    def open_spider(self, spider):
        self.connection = connection
        self.cur = connection.cursor()
        self.Redis = RedisOpera('insert')

    def close_spider(self, spider):
        self.cur.close()

    def process_item(self, item, spider):

        self.Redis.write(item['url'])

        uuid = str(uuid4()).replace("-", "")
        title = item['title']
        detail = item['detail']
        if detail:
            detail = detail.replace("'", "\'")

            # TODO channel_id 栏目id
            zhdj_cms_content_sql = f"""
    insert into zhdj_cms_content (
    id, title, short_title, short_txt, channel_id, 
    cover_picture, author, origin, 
    origin_url, published_at, status, content_type, external_url, flags, created_by, 
    created_at, updated_by, updated_at, belong_org_id, view_org_id, json_value, compilation_type, is_obligatory) 
    value ('{uuid}', '{title}', null , null, 'channel_id', 'cover_picture', 'author', 
    'origin','origin_url', '{datetime.now()}', '3', 'content_type', 'external_url', 4, '1', '{item["created_at"]}', '1', 
    '{datetime.now()}', 'belong_org_id', 'view_org_id', null, null, null)
            """
            zhdj_cms_content_detail_sql = f"""
    insert into zhdj_cms_content_detail (id, txt) value ('{uuid}', '{detail}')
    """

            try:
                # TODO need a transaction
                self.cur.execute(zhdj_cms_content_sql)
                self.cur.execute(zhdj_cms_content_detail_sql)
                self.connection.commit()
            except Exception as e:
                logging.error(e)
        else:
            logging.error(f"no content: {item}")

        return item
