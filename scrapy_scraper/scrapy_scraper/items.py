# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyScraperItem(scrapy.Item):
    batch=scrapy.Field()
    time=scrapy.Field()
    query=scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
    ago=scrapy.Field()

# class BatchItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     batch=scrapy.Field()
#     query=scrapy.Field()
#     title=scrapy.Field()
#     link=scrapy.Field()
#     ago=scrapy.Field()
