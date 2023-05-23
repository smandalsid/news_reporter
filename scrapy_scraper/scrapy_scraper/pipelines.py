# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class ScrapyScraperPipeline:

    def __init__(self):
        self.conn=MongoClient("localhost", 27017)
        self.db=self.conn["news"]


    def process_item(self, item, spider):
        item=dict(item)
        self.collection = self.db[item['ago']]
        self.collection.replace_one(
            {'title': item['title']},
            item,
            upsert=True
        )
        # self.collection.insert_one(dict(item))
        return item
