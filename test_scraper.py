import requests
from readability import Document
from basic_scraper import *
from news_extractor import *

url = 'http://www.nytimes.com'
page = Webpage(url)
article_candidates = get_articles_from_page_data(page)
print(article_candidates)
articles = [article_from_url(url) for url in article_candidates[:10]]
for article in articles:
    print(article.body)

