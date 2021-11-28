# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LifeweekItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题、作者、内容、创建时间、来源、点击量
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    createDate = scrapy.Field()
    source = scrapy.Field()
    hits = scrapy.Field()
