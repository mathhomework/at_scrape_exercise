from scrapy.selector import Selector
from scrapy.spider import Spider

class AT_Char_Spider(Spider):
    name = "char"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Category:Characters"
    ]

    def parse(self, response):
        sel = Selector(response)
        datas = sel.xpath("(//div[@class='mw-content-ltr'])[3]/table/tr/td/ul/li/a/text()").extract()
        print datas
        # for data in datas:
        #     name = data.xpath('text()').extract()
        #     print name