import scrapy
from scrapy.http import Request

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    # start_urls = [
    #     'http://gz.58.com/chuzu/pn1/'
    #     # 'http://gz.58.com/chuzu/pn2/'
    # ]

    def start_requests(self):
        pages = []
        for i in range(1, 10):
            url = 'http://gz.58.com/chuzu/pn%s/' % i
            page = scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        for i in range(5):
            urls = response.xpath('//tr[' + str(i + 1) + ']/td[2]/a[@class="t"]/@href').extract()
            for url in urls:
                yield Request(url, callback=self.parse2, dont_filter=True)

    def parse2(self,response):
        item = DmozItem()
        item['cost'] = response.xpath('//ul/li[1]/div/i/em/text()').extract()
        item['house'] = response.xpath('//ul/li[2]/div[@class="fl house-type c70"]/text()').extract()
        item['houseName'] = response.xpath('//ul/li[3]/div/a[@class="ablue"]/text()').extract()
        item['address'] = response.xpath('//ul/li[4]/div[@class="fl c70"]/text()').extract()
        item['houseDetail'] = response.xpath('//ul/li[5]/div/span[@class="inlineblock"]/text()').extract()
        return item


