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


class AT_Char_Spider_Detail(Spider):
    name = "char_detail"
    allowed_domains = ["adventuretime.wikia.com"]
    start_urls = [
        "http://adventuretime.wikia.com/wiki/Doctor_Princess"
    ]

    # name = Field()
    # sex = Field()
    # species = Field()
    # link = Field()
    # image = Field()
    # appearances = Field()

    def parse(self, response):
        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        categories = data.xpath("tr[position()>2]/td/b/text()").extract()
        info = data.xpath("tr[position()>2]/td/text()|//table[@class='infobox']/tr[position()>2]/td/a/text()|//table[@class='infobox']/tr[position()>2]/td/b/a/text()").extract()
        link = self.start_urls[0]
        info = [x for x in info if len(x) > 2]
        print "**********************************"
        for x in range(len(info)):
            if "\n" in info[x]:
                info[x] = info[x][:-1]
        print categories
        print info
        print "**********************************"

        # species = sel.xpath("(//table[@class='infobox']/tr[5]/td[2]/a/text()").extract()
        image = sel.xpath("//table[@class='infobox']/tr/td/a/img/@data-src").extract()
        # name = sel.xpath("//table[@class='infobox']/tr/th/font/text()").extract()
        # sex = sel.xpath("//table[@class='infobox]/tr[4]/td[2]/text()").extract()[0][1:-1]

        # print link, image, categories,info