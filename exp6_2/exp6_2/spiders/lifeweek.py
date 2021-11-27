import scrapy


class LifeweekSpider(scrapy.Spider):
    name = 'lifeweek'
    allowed_domains = ['www.lifeweek.com.cn']
    start_urls = ['http://www.lifeweek.com.cn/']

    def parse(self, response):
        pass
