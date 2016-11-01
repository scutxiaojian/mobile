import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://gz.58.com/zufang/27713096283825x.shtml?psid=151839647193713230787979671&ClickID=11&cookie=market|b-31580022738699-me-f-824.bdpz_biaoti|http://bzclk.baidu.com/adrc.php?t=06KL00c00fZy_wm0rEGN0nW_R00FnKIm00000KN9uW3000005m1X-I.THYdrnv__tT0UWdBmy-bIfK15ywWP1FBuh7-nj0snH0LPjm0IHdjPYNKnRDvwWbLnYwaPRu7f104PHnYwWKjwRR3nH-jwfK95gTqFhdWpyfqnW6znjm3nHTdPBusThqbpyfqnHm0uHdCIZwsrBtEpMNVTa4_Iy49QWR3QhPEUiq15LPsUHdBQHnkPH6snjczP1n3PWb4Qyd-QymVrjcYFhPC5yFbTZGxmh-9ULwG0APzm1Yvnj03ns&tpl=tpl_10085_14394_1&l=1046896917&ie=utf-8&f=8&tn=baidu&wd=58%E5%90%8C%E5%9F%8E&oq=58%E5%90%8C%E5%9F%8E&rqlang=cn&cq=d0d2ce2bdc9bc2bca1f3ac9e4adb4274&srcid=20986&rt=%E7%9B%B8%E5%85%B3%E7%BD%91%E7%AB%99&euri=8364412a5b9c46af97061c60b7f362e7|15EUFlgXMAxPMXywf8ppMA==&PGTID=0d3090a7-0000-3416-2b7f-4f0ce024776b&version=A&apptype=0&entinfo=27713096283825_0&iuType=gz_2&pubid=3922306&local=3&trackkey=27713096283825_5812248f-9766-400e-97bc-5980249efd96_20161031195204_1477914724226&fcinfotype=gz"
    ]

    def parse(self, response):
        # for sel in response.xpath('//ul/li'):

        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item
        # html/body/div[7]/div[3]/div[3]/ul/li[1]/div/i/em
        # ul/li[2]/div/text()
        item = DmozItem()
        item['cost'] = response.xpath('//ul/li[1]/div/i/em/text()').extract()
        item['house'] = response.xpath('//ul/li[2]/div[@class="fl house-type c70"]/text()').extract()
        return item


