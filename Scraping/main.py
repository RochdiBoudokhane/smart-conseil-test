from scraping import Scraper

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

posts = Scraper()

db = client["Facebook"]
msg_collection = db["posts"]

def read_items(tags):
  ScrapingPost = posts.scrapedata(tags)
  result = msg_collection.insert_many(ScrapingPost)
  print('*******', result.inserted_ids)
  x = msg_collection.find_one()
  print(x)

  return ScrapingPost

read_items('Tunisia')

