from scrapy.selector import Selector
from scrapy.spider import Spider
from at_scrape_exercise.items import AT_Char_Item
import re


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
        # for datum in data:
        #     item = AT_Char_Item()
        #     x = datum.xpath("text()").extract()
        #     if "User" not in x[0]:
        #         item['name'] = x[0]
        #         item['link'] = datum.xpath("@href").extract()[0]
        #         items.append(item)
        # return items

        with open('characters.txt', 'a') as f:
            for datum in data:
                x = datum.xpath("text()").extract()
                if "User" not in x[0]:
                    f.write("http://adventuretime.wikia.com{}\n".format(datum.xpath("@href").extract()[0]))
            f.close()


class AT_Char_Spider_Detail(Spider):
    name = "char_detail"
    allowed_domains = ["adventuretime.wikia.com"]
    characters = open("characters_test.txt")
    # start_urls = [url.strip() for url in characters.readlines()]
    start_urls = [
        # "http://adventuretime.wikia.com/wiki/Doctor_Princess",
        "http://adventuretime.wikia.com/wiki/Finn",
        "http://adventuretime.wikia.com/wiki/Marceline",
        "http://adventuretime.wikia.com/wiki/Breakfast_Princess",
        "http://adventuretime.wikia.com/wiki/Abe_Lincoln",
    ]

    def parse(self, response):

        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        categories = data.xpath("tr[position()>2]/td/b/text()").extract()
        link = self.start_urls[0]

        species = data.xpath("tr/td/a[../../td/b/text()='Species']/text()|tr[td/b/text()='Species']/td/text()[normalize-space()]").extract()
        print species
        # returns [u'Vampire', u'Demon']

        # the occupation below does not take into account a tags... so Marceline's Henchmen would just be something like 's henchmen
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/text()").extract()
        # occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/descendant::text()").extract()
        # this is more specific than the below because it does not matter where the extra space after occupation is
        # occupation = data.xpath("tr[td/b/text()='Occupation ']/td[position()>1]/text()").extract()
        occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]").extract()[0]

        print "***********OCCUPATION******************"
        for x in str(occupation).split("<br>"):
            y = re.sub('<[^>]*>', '', re.sub('\(.*?\)', '', x)).strip().rstrip(",")
            print y
        print "**********END OCCUPATION**************"

        sex = data.xpath("normalize-space(tr[td/b/text()='Sex']/td[position()>1]/text())").extract()
        print sex

        name = data.xpath("normalize-space(tr[td/b/text()='Name']/td[position()>1]/text())").extract()
        print name

        relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/a/text()").extract()
        print relatives
        print "WOWLOWLWOWLWOLWOW"
        link = response.request.url
        print link

        appearances = sel.xpath("//div[@id='mw-content-text']/ul[1]/li/a/text()").extract()
        print appearances
        image = data.xpath("tr/td/a[@class='image image-thumbnail']/@href").extract()
        print image
