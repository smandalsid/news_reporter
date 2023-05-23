from support.constants import *
from support.functions import *
from pymongo import MongoClient


client=MongoClient("mongodb://localhost:27017")
bot=Scraping(client["news_db"])
bot.land_page(URL)
# bot.scroll()
# bot.getarticles()
# bot.quit()
