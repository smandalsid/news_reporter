import scrapy
from ..items import ScrapyScraperItem
from datetime import datetime, timedelta

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = []
    # start_urls = ["https://www.moneycontrol.com/news/technology/"]

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def __init__(self):
        self.start_urls=self.get_company()

    def get_company(self):
        self.inp=input("Enter first query: ")
        self.query="https://news.google.com/search?q="+self.inp+"&hl=en-IN&gl=IN&ceid=IN%3Aen"
        return [self.query]

    def parse(self, response):

        items=ScrapyScraperItem()

        # boxes=response.css('li.clearfix')
        
        # for box in boxes:
        #     items['title']=box.xpath('./h2/a/text()').extract()
        #     yield items
            
        boxes=response.xpath('//article[@jscontroller="HyhIue"]')
        for box in boxes:
            heading=box.css('h3 a::text').get()
            link="https://news.google.com"+box.css('h3 a').attrib['href'][1:]
            ago=box.css('time::text').get()

            if "days" not in ago:
                ago=str(datetime.now())
            else:
                ago=str(datetime.now()-timedelta(days=int(ago[0])))
            ago=ago[:10]
            items['query']=self.inp
            items['title']=heading
            items['link']=link
            items['ago']=ago
            yield items
            print("\n")

        self.inp=input("Enter next search query: ")
        if(self.inp=="q"):
            return
        next_page="https://news.google.com/search?q="+self.inp+"&hl=en-IN&gl=IN&ceid=IN%3Aen"
        yield response.follow(next_page, callback=self.parse)
