from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import time
from support.constants import *

class Scraping(webdriver.Chrome):

    def __init__(self, client:MongoClient):
        options=webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir=/home/siddharth/.config/google-chrome/Default")
        #options.add_argument('proxy-server=106.122.8.54:3128')
        #options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--headless")
        super(Scraping, self).__init__(options=options)
        self.implicitly_wait(20)
        self.maximize_window()
        self.client=client

    
    def land_page(self, url):

        # self.get(url)

        for s in SEARCHES:
            self.search(s)
            self.scroll()
            self.getarticles(s)

    def search(self, s):
        self.get(URL)
        search=self.find_element(By.XPATH, "//input[@jsname='dSO9oc']")
        search.click()
        search.clear()
        search.send_keys(s)
        search.send_keys(Keys.ENTER)


    def scroll(self):
        time.sleep(5)
        self.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def getarticles(self, s):
        self.collection=self.client[s]
        print("#######", s, "#######")
        boxes=self.find_elements(By.XPATH, "//article[@jscontroller='HyhIue']")
        print(len(boxes))
        # print(boxes[0].text)
        for ind, box in enumerate(boxes):
            if ind==10:
                break
            headline=box.find_element(By.TAG_NAME, 'h3').text
            link=box.find_element(By.TAG_NAME, 'a').get_attribute('href')
            old=box.find_element(By.TAG_NAME, 'time').text
            if('days' in old):
                # day=[int(i) for i in old.split() if i.isdigit()][[0]]
                # if day>1:
                continue

            if '...' in headline:
                self.execute_script("window.open('');")
                self.switch_to.window(self.window_handles[1])
                self.get(link)
                headline=WebDriverWait(self, 15).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
                headline=headline.text
                self.close()
                self.switch_to.window(self.window_handles[0])


            d={
                "comp": s,
                "headline":headline,
                "link":link,
                "ago":old,
            }
            print(d, "\n")
            self.collection.insert_one(d)

    def quit(self):
        while True:
            pass