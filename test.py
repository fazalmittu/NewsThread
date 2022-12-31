import os
from dotenv import load_dotenv
import json
from newsapi.newsapi_client import NewsApiClient
import datetime
# from draft_thread import generate_thread

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
newsapi = NewsApiClient(NEWSAPI_KEY)

# category options: business, entertainment, general, health, science, sports, technology

def get_new_articles(num_articles=1):

    # all_articles = newsapi.get_everything(domains="wsj.com, forbes.com, bbc.com",
    #                                     from_param=f"{datetime.datetime.now():%Y-%m-%d}",
    #                                     language="en",
    #                                     sort_by="relevancy",
    #                                     page_size=num_articles)

    all_articles = newsapi.get_everything(q='iPhone',
                                      domains="wsj.com",
                                      from_param='2022-12-28',
                                      language="en",
                                      sort_by="relevancy",
                                      page_size=1)

    print(json.dumps(all_articles, indent=4))

get_new_articles(1)