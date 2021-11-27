# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import json


class Exp61Pipeline(object):
    def __init__(self):

        # python3保存文件 必须需要'wb' 保存为json格式
        self.f = open("article_pipeline.json",'ab')

    def process_item(self, item, spider):

        # 读取item中的数据 并换行处理
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content.encode('utf-8'))
        return item

    def close_spider(self,spider):
        # 关闭文件
        self.f.close()





