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
        # "http://adventuretime.wikia.com/wiki/Finn",
        # "http://adventuretime.wikia.com/wiki/Marceline",
        # "http://adventuretime.wikia.com/wiki/Breakfast_Princess",
        "http://adventuretime.wikia.com/wiki/Abe_Lincoln",
    ]


    def parse(self, response):

        sel = Selector(response)
        data = sel.xpath("//table[@class='infobox']")
        categories = data.xpath("tr[position()>2]/td/b/text()").extract()
        # info = data.xpath("tr[position()>2]/td/text()|//table[@class='infobox']/tr[position()>2]/td/a/text()|//table[@class='infobox']/tr[position()>2]/td/b/a/text()").extract()
        link = self.start_urls[0]
        # info = [x for x in info if len(x) > 2]


        species = data.xpath("tr/td/a[../../td/b/text()='Species']/text()|tr[td/b/text()='Species']/td/text()").extract()
        print species
        # returns [u'Vampire', u'Demon']

        occupation = data.xpath("tr[td/b[contains(.,'Occupation')]]/td[position()>1]/text()").extract()
        # this is more specific than the below because it does not matter where the extra space after occupation is
        # occupation = data.xpath("tr[td/b/text()='Occupation ']/td[position()>1]/text()").extract()
        print occupation

        sex = data.xpath("tr[td/b/text()='Sex']/td[position()>1]/text()").extract()
        print sex

        name = data.xpath("tr[td/b/text()='Name']/td[position()>1]/text()").extract()
        print name

        relatives = data.xpath("tr[td/b/text()='Relatives']/td[position()>1]/a/text()").extract()
        print relatives
        print "WOWLOWLWOWLWOLWOW"
        link = response.request.url
        print link

        # print "INFO***********"
        # print info
        # print "=================="

        # sometimes data has spaces in front or new lines escape char at the end, so this removes it.
        # commented out because it was referring to unused info. use this for new dict data.
        # for x in range(len(info)):
        #     if info[x][0] == " ":
        #         info[x] = info[x][1:]
        #     if "\n" in info[x]:
        #         info[x] = info[x][:-1]

        # combined_info = dict(zip(categories, info))
        #
        appearances = sel.xpath("//div[@id='mw-content-text']/ul[1]/li/a/text()").extract()
        print appearances
        image = data.xpath("tr/td/a[@class='image image-thumbnail']/@href").extract()
        print image
        # name = combined_info["Name"]
        # if "Species" in combined_info:
        #     species = combined_info["Species"]
        # if "Sex" in combined_info:
        #     sex = combined_info["Sex"]
        # if "Introduced in" in combined_info:
        #     introduced = combined_info["Introduced in"]
        # print "************************"
        # print name
        # print species
        # print sex
        # print introduced
        # print image
        # print "************************"
        # print combined_info