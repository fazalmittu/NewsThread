import os
from dotenv import load_dotenv
import json
from newsapi import NewsApiClient

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
newsapi = NewsApiClient(NEWSAPI_KEY)

# category options: business, entertainment, general, health, science, sports, technology

# top_headlines = newsapi.get_top_headlines(category='business',
#                                           q='bitcoin')

all_articles = newsapi.get_everything(q='iPhone',
                                      domains="wsj.com",
                                      from_param='2022-12-28',
                                      language="en",
                                      sort_by="relevancy",
                                      page_size=1)

print(json.dumps(all_articles, indent=4))

