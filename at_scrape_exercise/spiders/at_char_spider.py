from scrapy.selector import Selector
from scrapy.spider import Spider
from at_scrape_exercise.items import AT_Char_Item


class AT_Char_Spider(Spider):
    name = "char"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Category:Characters",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Donny+%28character%29#mw-pages",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Jungle+Princess#mw-pages",
        "http://adventuretime.wikia.com/wiki/Category:Characters?pagefrom=Rock+Giant#mw-pages"

    ]

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("(//div[@class='mw-content-ltr'])[3]/table/tr/td/ul/li/a")
        items = []
        for datum in data:
            item = AT_Char_Item()
            x = datum.xpath("text()").extract()
            if "User" not in x[0]:
                item['name'] = x[0]
                item['link'] = datum.xpath("@href").extract()[0]
                items.append(item)
        return items