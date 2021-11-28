import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider, Rule
from ..items import LifeweekItem


class LifeweekSpider(CrawlSpider):
    name = 'lifeweek'
    allowed_domains = ['lifeweek.com.cn']
    start_urls = ['http://www.lifeweek.com.cn/society/']
    # restrict_xpaths = '//div[@id="content"]//ul//li//a/@href'
    rules = (
        Rule(LinkExtractor(allow=('([0-9]{5}.shtml)$',)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = LifeweekItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # 获取标题、作者、内容、创建时间、来源、点击量
        item['title'] = response.xpath('//h1/text()').extract()
        item['author'] = response.xpath('//h5//text()').extract()[2]
        item['content'] = response.xpath('//article/p//text()').extract()
        item['createDate'] = response.xpath('//h5//text()').extract()[0]
        item['source'] = response.xpath('//h5//text()').extract()[-2]
        item['hits'] = response.xpath('//div[@class="like mag10"]/span/text()').extract()
        print(item)
        yield item
