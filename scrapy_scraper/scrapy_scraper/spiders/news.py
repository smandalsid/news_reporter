import scrapy
from ..items import ScrapyScraperItem
from datetime import datetime, timedelta
import time
import requests
import logging
from scrapy.utils.log import configure_logging 

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = []
    # start_urls = ["https://www.moneycontrol.com/news/technology/"]

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        level=logging.ERROR,
        filename='news.log',
        format=f'[%(asctime)s] %(levelname)s: %(message)s',
    )

    def __init__(self):
        # self.batch=1
        with open("file.txt") as file: 
            data = file.read()
            self.batch=int(data[7:])
        self.companies=['google', 'meta', 'apple', 'microsoft']
        self.comp=0
        self.start_urls=self.get_company()

    def get_company(self):
        # self.inp=input("Enter first query: ")
        self.query="https://news.google.com/search?q="+self.companies[self.comp]+"&hl=en-IN&gl=IN&ceid=IN%3Aen"
        self.comp+=1
        return [self.query]

    def parse(self, response):

        items=ScrapyScraperItem()
        # items2=BatchItem()

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

            items['query']=self.companies[self.comp-1]
            items['batch']=str(self.batch)
            items['title']=heading
            items['link']=link
            items['ago']=ago
            items['time']=str(datetime.now())

            requests.post("http://127.0.0.1:8000/api/"+items['query']+"/", {'batch': str(self.batch), 'title': items['title'], 'link': items['link'], 'ago': items['ago'], 'time': items['time']})

            yield items

            # items2['query']=self.companies[self.comp-1]
            # items2['batch']=str(self.batch)
            # items2['title']=heading
            # items2['link']=link
            # items2['ago']=ago
            # yield items1, items2

            # print("\n")

        # self.batch+=1
        if self.comp!=4:
            self.inp=self.companies[self.comp]
            self.comp+=1
        elif self.comp==4:
            # self.inp=self.companies[0]
            # self.comp=1
            # self.batch+=1
            # if(self.batch==3):
            #     return
            # time.sleep(2)
            with open("file.txt", "w") as f:
                f.write("Batch: "+str(self.batch+1))
            return

        next_page="https://news.google.com/search?q="+self.inp+"&hl=en-IN&gl=IN&ceid=IN%3Aen"
        yield response.follow(next_page, callback=self.parse)
