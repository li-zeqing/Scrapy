# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 提取书籍信息包括：书名、抢购价、定价、作者、出版时间、出版社、评论数量
    #                bookName,BuyPrice,pricing,author,PubDate,press,CommentNumber
    bookName = scrapy.Field()
    BuyPrice = scrapy.Field()
    pricing = scrapy.Field()
    author = scrapy.Field()
    PubDate = scrapy.Field()
    press = scrapy.Field()
    CommentNumber = scrapy.Field()

