import scrapy
from ..items import LifeweekItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class LifeweekSpider(CrawlSpider):
    name = 'lifeweek'
    allowed_domains = ['www.lifeweek.com.cn']
    start_urls = ['http://www.lifeweek.com.cn/society/']
    rules = [Rule(LinkExtractor(allow='(.shtml)$',restrict_xpaths='//div[@id="content"]//ul//li//a/@href'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        item = LifeweekItem()
        # 获取标题、作者、内容、创建时间、来源、点击量
        item['title'] = response.xpath('//h1').extract()
        item['author'] = response.xpath('//h5').extract()
        item['content'] = response.xpath('//article/p').extract()
        item['createDate'] = response.xpath('//h5').extract()
        item['source'] = response.xpath('//h5').extract()
        item['hits'] = response.xpath('//div[@class="like mag10"]/span').extract()
        yield item