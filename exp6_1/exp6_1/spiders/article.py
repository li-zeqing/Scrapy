import scrapy
from ..items import Article


# from exp6_1.exp6_1.items import Article


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['dangdang.com']

    def start_requests(self):
        cookies = {
            'MDD_sid': 'bdfb0068f4620e228f890a2c2bb0a4a7',
            'MDD_permanent_id': '20211109214555026931004031245412084',
            'MDD_province_id': '111',
            'MDD_province_str': '%E5%8C%97%E4%BA%AC',
            'MDD_city_id': '1',
            'MDD_city_str': '%E5%8C%97%E4%BA%AC%E5%B8%82',
            'MDD_area_id': '1110101',
            'MDD_area_str': '%E4%B8%9C%E5%9F%8E%E5%8C%BA',
            '__permanent_id': '20211109214557735292272713369115686',
            'from': '460-5-biaoti',
            'MDD_channelId': '70000',
            'MDD_fromPlatform': '307',
            'dangdang.com': 'email=MTU4MjA2ODE4MDExMzUzMEBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=2596550194389&customerid=rqrEpKkNVn2fRweK1Gwgtg==&viptype=19xTTUluvhg=&show_name=158****1801',
            'order_follow_source': 'P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.af0000jT3UUcPe3KL3ALSG5SoRAxAUXRLLtB2YR7CbgYnphA-F88J8Y4XI4q1LzBuxgdw3hSE%7C%230-%7C-',
            'ddscreen': '2',
            '__ddc_1d': '1637938106%7C!%7C_utm_brand_id%3D11106',
            '__ddc_24h': '1637938106%7C!%7C_utm_brand_id%3D11106',
            '__ddc_15d': '1637938106%7C!%7C_utm_brand_id%3D11106',
            '__ddc_15d_f': '1637938106%7C!%7C_utm_brand_id%3D11106',
            'dest_area': 'country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0',
            'login_dang_code': '2021112622484692124770303653be06',
            'sessionID': 'pc_dfb9f8b3461cb31007183795f892242c33c688464b9da84e2705fb76553a240',
            'USERNUM': 'T0LSFHA8bN9vwTOqyqQHlQ==',
            'login.dangdang.com': '.ASPXAUTH=sxQ9pMW1plLNXGgMu6crySoyF6bMnKWCd+68R2KfG5HVU3fNEuOSqA==',
            '__visit_id': '20211126230106863412739642947472345',
            '__out_refer': '1637938867%7C!%7Cwww.baidu.com%7C!%7C',
            'LOGIN_TIME': '1637938873769',
            '__rpm': '%7Cs_112100...1637938878793',
            'search_passback': '91da83bf7b229c4fc0f6a061fc01000055776800c0f6a061',
            '__trace_id': '20211126230121796378393896676832755',
            'pos_9_end': '1637938881992',
            'pos_0_start': '1637938882014',
            'pos_0_end': '1637938882020',
            'ad_ids': '3643545%2C5626087%2C3643543%2C3608930%2C3687921%2C3643544%7C%233%2C3%2C3%2C3%2C3%2C1'
        }


        start_urls = ['http://search.dangdang.com/?key=python&act=input']
        for i in range(2, 3):
            url_ = 'http://search.dangdang.com/?key=python&act=input&page_index={}'.format(i)
            start_urls.append(url_)

        print(len(start_urls))
        for url in start_urls:
            yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)
            # yield Request(detailUrl, headers=headers, cookies=cookies, callback=self.detail_parse,
            #               meta={'myItem': item}, dont_filter=True)

    def parse(self, response):
        cookies = {
            'MDD_sid': 'bdfb0068f4620e228f890a2c2bb0a4a7',
            'MDD_permanent_id': '20211109214555026931004031245412084',
            'MDD_province_id': '111',
            'MDD_province_str': '%E5%8C%97%E4%BA%AC',
            'MDD_city_id': '1',
            'MDD_city_str': '%E5%8C%97%E4%BA%AC%E5%B8%82',
            'MDD_area_id': '1110101',
            'MDD_area_str': '%E4%B8%9C%E5%9F%8E%E5%8C%BA',
            '__permanent_id': '20211109214557735292272713369115686',
            'ddscreen': '2',
            'from': '460-5-biaoti',
            'order_follow_source': 'P-460-5-bi%7C%231%7C%23www.baidu.com%252Fother.php%253Fsc.Ks00000O2YI2AYqt4JNqlfVDrxw59Hvw_UE_HCA_LqZzMfw_2LjdhK7zQqrQmAY3aEYUZ6ZCv%7C%230-%7C-',
            'dest_area': 'country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0',
            'MDD_channelId': '70000',
            'MDD_fromPlatform': '307',
            'producthistoryid': '1901239653',
            'pos_6_start': '1637763884783',
            'pos_6_end': '1637763884980',
            'pos_0_end': '1637764926808',
            'pos_9_end': '1637764930062',
            'ad_ids': '2760118%2C2760100%2C2737748%2C2737746%2C2737745%2C2737744%7C%232%2C1%2C3%2C3%2C2%2C2',
            '__visit_id': '20211124224323530510311997178769756',
            '__out_refer': '1637765004%7C!%7Cwww.baidu.com%7C!%7C',
            'sessionID': 'pc_f57b3a4ee2c66fd679805bd96e206ed594a473774f7de0a3560d95d02cb50200',
            'USERNUM': 'T0LSFHA8bN9vwTOqyqQHlQ==',
            'login.dangdang.com': '.ASPXAUTH=sxQ9pMW1plLNXGgMu6crySoyF6bMnKWCd+68R2KfG5HVU3fNEuOSqA==',
            'dangdang.com': 'email=MTU4MjA2ODE4MDExMzUzMEBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=2596550194389&customerid=rqrEpKkNVn2fRweK1Gwgtg==&viptype=19xTTUluvhg=&show_name=158****1801',
            '__rpm': '%7Cmix_317715...1637765870706',
            '__trace_id': '20211124225753539338536826068858915'
        }

        Url_list = response.xpath('//ul[@class="bigimg"]//li/p[@class="name"]/a/@href').extract()
        print("此页面共有{}个网页链接".format(len(Url_list)))
        for url in Url_list:
            print(url)
            url_ = 'http:' + url
            # print(url_)
            yield scrapy.Request(url=url_, cookies=cookies, callback=self.parse2)

    def parse2(self, response):
        article = Article()
        article['bookName'] = response.xpath('//div[@class="name_info"]/h1/@title').extract()
        article['BuyPrice'] = response.xpath('//p[@id="dd-price"]/text()').extract()[1]
        article['pricing'] = response.xpath('//div[@id="original-price"]/text()').extract()[1]
        article['author'] = response.xpath('//span[@id="author"]//text()').extract()
        article['PubDate'] = response.xpath('//div[@class="messbox_info"]/span[last()]/text()').extract()
        article['press'] = response.xpath('//div[@class="messbox_info"]/span[@dd_name="出版社"]/a/text()').extract()
        article['CommentNumber'] = response.xpath('//span[@id="messbox_info_comm_num"]/a/text()').extract()

        return article
